#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cdp_backend.infrastructure import CDPStack
from pulumi import export

###############################################################################

cdp_stack = CDPStack(
    gcp_project_id="cdp-king-county-b656c71b",
    municipality_name="King County",
    firestore_location="us-central",
    hosting_github_url="https://github.com/CouncilDataProject/king-county",
    hosting_web_app_address="https://councildataproject.github.io/king-county",
    governing_body="county council",
)

export("firestore_address", cdp_stack.firestore_app.app_id)
export("gcp_bucket_name", cdp_stack.firestore_app.default_bucket)
