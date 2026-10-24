from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from hashlib import sha256
from datetime import datetime,timezone
import json
target=Path('C:/Users/14383/Desktop/汇率智能体网页')
original=Path('C:/Users/14383/Desktop/汇率智能体/release-v2/ExchangeRateAgent')
out=target/'local-data'/'downloads'
out.mkdir(parents=True,exist_ok=True)
archive=out/'ExchangeRateAgent-Windows.zip'
with ZipFile(archive,'w',ZIP_DEFLATED,compresslevel=9) as z:
    files=[original/'ExchangeRateAgent.exe']+[p for p in (original/'_internal').rglob('*') if p.is_file()]
    for p in files:z.write(p,Path('ExchangeRateAgent')/p.relative_to(original))
    z.write(Path('C:/Users/14383/Desktop/汇率智能体/使用说明.md'),Path('ExchangeRateAgent')/'使用说明.md')
with ZipFile(archive) as z:
    assert z.testzip() is None
    assert not any('settings.dpapi' in n or 'default-model.json' in n or 'fxagent.sqlite' in n for n in z.namelist())
manifest={'bytes':archive.stat().st_size,'sha256':sha256(archive.read_bytes()).hexdigest(),'prepared_at':datetime.now(timezone.utc).isoformat()}
(out/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print('Original Windows app packaged; archive valid; personal runtime data excluded. Size bytes:',manifest['bytes'])
