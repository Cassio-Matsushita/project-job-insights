from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    all_salaries = set()
    all_jobs = read(path)
    for job in all_jobs:
        if job["max_salary"].isdigit():
            all_salaries.add(job["max_salary"])
    max_salary = max([int(i) for i in all_salaries])
    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    all_salaries = set()
    all_jobs = read(path)
    for job in all_jobs:
        if job["min_salary"].isdigit():
            all_salaries.add(job["min_salary"])
    min_salary = min([int(i) for i in all_salaries])
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        max = int(job["max_salary"])
        min = int(job["min_salary"])
        int(salary)
    except Exception:
        raise ValueError()
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    if max < min:
        raise ValueError()
    return min <= int(salary) <= max


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    salary_filter = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_filter.append(job)
        except ValueError:
            pass
    return salary_filter
