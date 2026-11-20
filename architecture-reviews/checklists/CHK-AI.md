---
id: CHK-AI
type: checklist
title: AI System Review Checklist
status: draft
version: 0.9
owner: Enterprise Security Architecture
applies_to:
  components: [ai-ml]
summary: Reviewer questions for LLM / ML systems.
---
- [ ] Approved model provider (SEC-AI-001.R1)
- [ ] Prompt-injection threat modelled; outputs validated before actions (SEC-AI-001.R2)
- [ ] Agent tools scoped; human approval for destructive actions (SEC-AI-001.R3)
- [ ] No restricted data to external models without DPA (SEC-AI-001.R4)
