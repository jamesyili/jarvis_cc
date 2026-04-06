# Primers • Pandas Tips

**Source:** https://aman.ai/primers/pandas-tips/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Change Values](#change-values)
  + [`pd.DataFrame.pipe`: Increase the Readability of your Code when Applying Multiple Functions to a DataFrame¶](#pddataframepipe-increase-the-readability-of-your-code-when-applying-multiple-functions-to-a-dataframe)
  + [`Deepchecks`: Check Category Mismatch Between Train and Test Set](#deepchecks-check-category-mismatch-between-train-and-test-set)
* [References and credits](#references-and-credits)
* [Citation](#citation)

## Change Values

### `pd.DataFrame.pipe`: Increase the Readability of your Code when Applying Multiple Functions to a DataFrame¶

* If you want to increase the readability of your code when applying multiple functions to a DataFrame, use pands.DataFrame.pipe method.

```
pip3 install TextBlob

from textblob import TextBlob
import pandas as pd 

def remove_white_space(df: pd.DataFrame):
    df['text'] = df['text'].apply(lambda row: row.strip())
    return df

def get_sentiment(df: pd.DataFrame):
    df['sentiment'] = df['text'].apply(lambda row:
                                    TextBlob(row).sentiment[0])
    return df

df = pd.DataFrame({'text': ["It is a beautiful day today  ",
                        "  This movie is terrible"]})

df = (df.pipe(remove_white_space)
    .pipe(get_sentiment)
)

df

#                           text  sentiment
# 0  It is a beautiful day today       0.85
# 1       This movie is terrible      -1.00
```

### `Deepchecks`: Check Category Mismatch Between Train and Test Set

* Sometimes, it is important to know if your test set contains the same categories in the train set. If you want to check the category mismatch between the train and test set, use Deepchecks’s [CategoryMismatchTrainTest](https://docs.deepchecks.com/en/stable/).
* In the example below, the result shows that there are 2 new categories in the test set. They are ‘d’ and ‘e’.

```
pip3 install deepchecks

from deepchecks.checks.integrity.new_category import CategoryMismatchTrainTest
from deepchecks.base import Dataset
import pandas as pd
train = pd.DataFrame({"col1": ["a", "b", "c"]})
test = pd.DataFrame({"col1": ["c", "d", "e"]})

train_ds = Dataset(train, cat_features=["col1"])
test_ds = Dataset(test, cat_features=["col1"])
CategoryMismatchTrainTest().run(train_ds, test_ds)
# Category Mismatch Train Test: {'col1': {'n_new': 2, 'n_total_samples': 3, 'new_categories': ['d', 'e']}}
```

## References and credits

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledPandasTips,
  title   = {NumPy Tips},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
