"""Skill Mismatch metric definitions (BRD 4.5, AC-06)."""
from typing import Iterable, Set

def supply_share(credits_for_skill: float, total_required_credits: float) -> float:
    """Supply share (s): fraction of required credits mapped to skill k in program c."""
    if not total_required_credits or total_required_credits <= 0:
        return 0.0
    return float(credits_for_skill) / float(total_required_credits)

def demand_share(freq_skill: float, total_freq: float) -> float:
    """Demand share (d): normalized frequency/importance of skill k in role r."""
    if not total_freq or total_freq <= 0:
        return 0.0
    return float(freq_skill) / float(total_freq)

def gap_score(d: float, s: float) -> float:
    """Gap Score = d - s.
    Positive = Market demands more than taught (Skill Shortage).
    Negative = Taught more than market demands (Curriculum Excess).
    """
    return float(d) - float(s)

def coverage_at_n(top_n_skills: list[str], skills_with_supply: Set[str]) -> float:
    """Coverage@N: fraction of top-N market skills that have supply share s > 0."""
    n = len(top_n_skills)
    if n == 0:
        return 0.0
    covered = sum(1 for sk in top_n_skills if sk in skills_with_supply)
    return covered / n
