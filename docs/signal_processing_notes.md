# Signal Processing Notes

Low-cost optical sensors such as MAX30102 exhibit significant noise and baseline drift.

## Observed Problems
- DC offset due to ambient light and sensor placement
- High-frequency noise
- Unstable peak detection

## Applied Solutions
- DC removal using moving average subtraction
- Experimental adaptive peak detection
- Empirical tuning based on real-world measurements

> Classical textbook filters were insufficient; therefore, an experimentally adjusted approach was used.
