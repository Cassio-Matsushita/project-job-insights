from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    unique_industry = set()
    all_jobs = read(path)
    for job in all_jobs:
        if not job["industry"] == "":
            unique_industry.add(job["industry"])
    return unique_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    jobs_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_by_industry.append(job)
    return jobs_by_industry
