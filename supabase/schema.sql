-- 在自己的 Supabase SQL 编辑器中执行；不会自动创建云端项目。
create table if not exists public.feedback (
 id uuid primary key,created_at timestamptz not null default now(),status text not null default 'new' check(status in ('new','done')),
 name text not null check(length(name) between 1 and 80),phone text not null default '',email text not null default '',experience text not null default '',suggestion text not null default '',problem text not null default '',consent boolean not null check(consent),
 check(length(phone)>0 or length(email)>0),check(length(experience)<=3000 and length(suggestion)<=3000 and length(problem)<=3000)
);
alter table public.feedback enable row level security;
revoke all on public.feedback from anon,authenticated;
grant all on public.feedback to service_role;
create table if not exists public.web_rate_limits(key text primary key,count integer not null,expires_at timestamptz not null);
alter table public.web_rate_limits enable row level security;
revoke all on public.web_rate_limits from anon,authenticated;
grant all on public.web_rate_limits to service_role;
create or replace function public.consume_web_limit(key_hash text,max_count integer) returns boolean language plpgsql security invoker set search_path='' as $$
declare current_count integer;
begin
 delete from public.web_rate_limits where expires_at<now();
 insert into public.web_rate_limits values(key_hash,1,now()+interval '30 minutes') on conflict(key) do update set count=public.web_rate_limits.count+1 returning count into current_count;
 return current_count<=max_count;
end;$$;
revoke all on function public.consume_web_limit(text,integer) from public,anon,authenticated;
grant execute on function public.consume_web_limit(text,integer) to service_role;
