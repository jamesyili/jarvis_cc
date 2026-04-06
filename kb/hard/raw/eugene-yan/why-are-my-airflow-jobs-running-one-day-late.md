# Why Are My Airflow Jobs Running “One Day Late”?

**Source:** https://eugeneyan.com//writing/why-airflow-jobs-one-day-late/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

“Why are our Airflow jobs always one day behind?”, a teammate asked. I popped open the Airflow dashboard; everything looked fine—I didn’t see any delay.

As he explained the delay he was seeing, I realized there are (at least) two ways to think about scheduling. The second way is so obvious (to me) that I forgot others may not be aware of its (i.e., expert blind spot).

## Cron

For most people, this is the first type of scheduling they come across, and operate on. [Cron](https://en.wikipedia.org/wiki/Cron) runs jobs at fixed intervals; you specify jobs in a `crontab` file, like below.

```
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of the month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │                                   7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * * <command to execute>
```

If something is scheduled for 2020-06-14 midnight, it starts at 2020-06-14 midnight—straightforward.

## Airflow (and ETL jobs)

Airflow works a bit differently. First, let’s see what happens. When you schedule a job for 2020-06-**14** (`Run` in the image below), it starts at 2020-06-**15** (`Started` in the image below).

An Airflow Job Seemingly One Day Late

Why is there a day’s delay? In Airflow, the job for 2020-06-14 can only trigger after 2020-06-14 2359hrs. In other words, the job only starts *after* the scheduled period (i.e., day of 2020-06-14) has ended. This so important that the [Airflow’s docs](https://airflow.apache.org/docs/stable/scheduler.html) has the following:

> **Let’s Repeat That.** The scheduler runs your job one schedule\_interval AFTER the start date, at the END of the period. - Airflow Docs

This is **not** a bug in Airflow or your DAGs.

## Why does it work like that?

I find that it’s helpful to explain it in terms of ETL (extract-transform-load). When you schedule a job for 2020-06-14, you want to process the data for that day; thus, it can only start when the day for 2020-06-14 ends, at 2020-06-15 0000hrs.

Thus, unlike cron jobs (which start at the scheduled time), Airflow jobs only start *after* the `period` of the scheduled time ends. If the period is an hour, it’ll start an hour after. If the period is a day, it’ll start a day after. And so on.

For a daily job, cron jobs run at the start of the day; Airflow jobs run at the end of the day.

If you stumbled on this looking for an answer, I hope this cleared things up. Else, comment below and I’ll help.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Jun 2020). Why Are My Airflow Jobs Running “One Day Late”?. eugeneyan.com.
> https://eugeneyan.com/writing/why-airflow-jobs-one-day-late/.

or

```
@article{yan2020airflow,
  title   = {Why Are My Airflow Jobs Running “One Day Late”?},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2020},
  month   = {Jun},
  url     = {https://eugeneyan.com/writing/why-airflow-jobs-one-day-late/}
}
```

  
Share on:
