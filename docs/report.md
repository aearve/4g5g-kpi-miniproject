# Network KPI Test Report (Simulated)

Data source: `data/sample_kpis.csv`

## Summary
- 4G: 4 samples, 1 failing
- 5G: 3 samples, 0 failing

## Thresholds
- 4G: latency<= 90.0ms, throughput>= 50.0Mbps, loss<= 1.0%
- 5G: latency<= 50.0ms, throughput>= 150.0Mbps, loss<= 0.6%

## Failures
- 4G @ 120 users: latency 105.0ms > 90.0ms; throughput 35.0Mbps < 50.0Mbps; packet_loss 1.7% > 1.0%
