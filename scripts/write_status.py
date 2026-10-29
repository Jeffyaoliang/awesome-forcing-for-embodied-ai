#!/usr/bin/env python3
"""Write a small GitHub Actions status report without external dependencies."""
import json, os, datetime, pathlib
name=os.environ["REPORT_NAME"]
status=os.environ.get("REPORT_RESULT","unknown")
p=pathlib.Path("reports")/(name+"-status.json")
p.parent.mkdir(parents=True,exist_ok=True)
data={"workflow":name,"result":status,"run_id":os.environ.get("GITHUB_RUN_ID"),"run_attempt":os.environ.get("GITHUB_RUN_ATTEMPT"),"sha":os.environ.get("GITHUB_SHA"),"event":os.environ.get("GITHUB_EVENT_NAME"),"updated_at":datetime.datetime.now(datetime.timezone.utc).isoformat()}
p.write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
print(p, status)
