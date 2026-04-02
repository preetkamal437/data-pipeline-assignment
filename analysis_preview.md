# Statistical Analysis Preview

## 1. Research Question

Is the average daily return of Bitcoin different on Fear days compared to Greed days?

---

## 2. Outcome Variable

* `btc_daily_return` (continuous variable)

---

## 3. Grouping Variable

* `fear_greed_label` (Fear vs Greed)

---

## 4. Binary Variable

* `positive_return`

This variable indicates whether Bitcoin had a positive return on a given day. It is useful for proportion-based statistical testing.

---

## 5. Hypotheses

### For t-test:

* Null Hypothesis (H0):
  There is no difference in mean BTC returns between Fear and Greed days.

* Alternative Hypothesis (H1):
  There is a difference in mean BTC returns between Fear and Greed days.

---

### For proportion z-test:

* Null Hypothesis (H0):
  The proportion of positive return days is the same for Fear and Greed.

* Alternative Hypothesis (H1):
  The proportion of positive return days differs between Fear and Greed.

---

## 6. Proposed Statistical Tests

* Two-sample t-test → compare mean returns
* Proportion z-test → compare probability of positive returns

---

## 7. Dataset Design Justification

The dataset includes:

* A continuous variable (`btc_daily_return`)
* A categorical grouping variable (`fear_greed_label`)
* A binary variable (`positive_return`)

This structure supports multiple statistical tests required for Part 2.

---
