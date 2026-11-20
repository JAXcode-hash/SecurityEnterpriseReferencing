---
id: SDR-001
type: decision
title: Use service mesh mTLS for Kubernetes east-west traffic
status: accepted
version: 1.0
owner: Security Design Authority
date: 2026-06-02
applies_to:
  hosting: [kubernetes]
summary: Mesh-issued SPIFFE identities with mTLS STRICT are the standard for in-cluster service-to-service auth; app-level JWT only as an addition.
---

## Context
Inconsistent service-to-service auth across clusters (SEC-IAM-001.R4).

## Decision
Mesh mTLS (STRICT) + AuthorizationPolicy allow-lists. Codified in `PAT-IAM-002`.

## Consequences
Platform team owns mesh; app teams own AuthorizationPolicy per service.
