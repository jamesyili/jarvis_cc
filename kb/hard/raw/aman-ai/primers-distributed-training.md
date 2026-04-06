# Primers • Distributed Training

**Source:** https://aman.ai/primers/ai/distributed-training/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [DeepSpeed and ZeRO-Offload](#deepspeed-and-zero-offload)
* [Citation](#citation)

## DeepSpeed and ZeRO-Offload

* Essentially, [DeepSpeed](https://www.deepspeed.ai/) is a library that helps train large to extremely large models (e.g., 1bn+ parameters) faster and using less GPU memory. This works by exploiting smart parallelism and better caching. It comes in the form of an extension to PyTorch.

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledModelCompression,
  title   = {Model Compression},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
