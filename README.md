# intent-drift-detector
A lightweight, off-chain behavioral intelligence system that detects when an entity stops behaving like its historical self.
# Intent Drift Detector

A lightweight, off-chain behavioral intelligence system that detects
when an entity stops behaving like its historical self.

This project is designed to be:
- Mobile-buildable
- Explainable
- Blockchain-friendly
- Training-free

## Concept

Behavior is modeled as a rolling "intent vector".
Drift is measured as distance between past and present intent.

## Use Cases

- DAO governance monitoring
- Wallet anomaly detection
- Sybil resistance signals
- Protocol access gating

## API

POST /detect

Returns a drift score and qualitative verdict.
