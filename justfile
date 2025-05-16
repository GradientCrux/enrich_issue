


deploy:
    gcloud functions deploy enrich_issue \
    --gen2 \
    --runtime=python310 \
    --region=YOUR_REGION \
    --trigger-topic=defect-detected \
    --entry-point=enrich_issue