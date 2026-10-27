# Data dictionary: synthetic security prices

FIN 494 — workspace module v1.1 — September 11, 2026

## Origin and permitted use

`sample_data/synthetic_prices.csv` was constructed for this teaching exercise with AI assistance and checked against the stated values. It contains **invented prices for two invented securities**. It was not downloaded from CRSP, WRDS, an exchange, or a market-data service. It is not evidence about investment performance.

You may copy this sample into your private course repository, run it in Codespaces, and use it as context in Cursor and your selected ChatGPT or Claude assistant for this assignment. These permissions apply to this synthetic sample; future licensed datasets have their own permissions.

## Structure

One row represents one security on one date. The unique key is `security_id` plus `date`. The file has **8 rows, 2 securities, 4 dates, and 1 missing price**. Dates run from September 1 through September 4, 2026. The original file is sorted by security and date, but both scripts sort explicitly before using a previous observation.

| Field | Type / units | Meaning |
|---|---|---|
| `security_id` | Text | Invented identifier: `SYN_A` or `SYN_B`; neither is a market ticker or CRSP identifier |
| `date` | ISO date, YYYY-MM-DD | Date assigned to the synthetic observation |
| `price` | Positive number, dollars per share | Invented price; a blank means missing, not zero |

`SYN_A` prices are 100, 102, 101, 105. `SYN_B` prices are 50, 49, missing, 51. The missing value is intentional. Preserve the original file.

## Calculated output

The scripts add `previous_price` and `price_return`, then select one security. `previous_price` is the preceding observation for the **same security**, ordered by date. The first observation has no previous price.

`price_return = price / previous_price - 1`

Returns are decimals: `0.02` means 2%; `-0.02` means -2%. If either required price is missing, leave the return missing. Do not fill a missing price with zero, carry another price forward, or drop a row before calculating the lag. Dropping rows can turn a return across a gap into an apparent single-period return.

This is a **price-return** calculation. The sample contains no dividend, split, or other corporate-action information; it does not support a total-return calculation. For production data, also establish the trading calendar, adjustment conventions, and whether observations are consecutive trading periods.

## File record

- Version: 1.1
- Format: UTF-8 CSV; comma separator; header row; blank missing price
- Source: course-created synthetic fixture; no external data source
- SHA-256 of the supplied file: `7f37d0efbc1c969ccee071cbf2dc6bf3fd60cfb92e23e84329d3cab513c6e387`

The checksum identifies the supplied bytes. You are not required to learn checksum commands in this module.
