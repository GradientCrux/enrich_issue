# enrich_issue

A minimal Google Cloud Function (2nd gen) that triggers from a Pub/Sub topic `defect-detected`, parses the incoming JSON into a Pydantic model, and prints the parsed issue.

## Requirements
- Python 3.9+
- [Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-python)
- [Pydantic](https://docs.pydantic.dev/)

## Local Development

Install dependencies:
```bash
pip install -r requirements.txt
```

Run locally:
```bash
functions-framework --target=enrich_issue --debug
```

## Deployment

Deploy to Google Cloud Functions (2nd gen):
```bash
gcloud functions deploy enrich_issue \
  --gen2 \
  --runtime=python310 \
  --region=YOUR_REGION \
  --trigger-topic=defect-detected \
  --entry-point=enrich_issue
```

Replace `YOUR_REGION` with your desired GCP region. 