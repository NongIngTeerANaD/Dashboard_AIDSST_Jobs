"""Unit tests for Skill Mismatch metric formulas (BRD section 4.5, AC-06)."""
import pytest
import pandas as pd


# ---------------------------------------------------------------------------
# Metric implementations (will be imported from app.metrics once created;
# for now defined here as reference implementations for testing)
# ---------------------------------------------------------------------------

def supply_share(credits_for_skill: float, total_required_credits: float) -> float:
    """Supply share (s): fraction of required credits mapped to skill k."""
    if total_required_credits == 0:
        return 0.0
    return credits_for_skill / total_required_credits


def demand_share(freq_skill: float, total_freq: float) -> float:
    """Demand share (d): normalized frequency of skill k in a role."""
    if total_freq == 0:
        return 0.0
    return freq_skill / total_freq


def gap_score(d: float, s: float) -> float:
    """Gap Score = d - s. Positive = market wants more than taught."""
    return d - s


def coverage_at_n(
    top_n_skills: list[str],
    skills_with_supply: set[str],
) -> float:
    """Coverage@N: fraction of top-N market skills that have s > 0."""
    n = len(top_n_skills)
    if n == 0:
        return 0.0
    covered = sum(1 for sk in top_n_skills if sk in skills_with_supply)
    return covered / n


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestSupplyShare:
    def test_basic(self):
        assert supply_share(3, 30) == pytest.approx(0.1)

    def test_zero_total(self):
        assert supply_share(5, 0) == 0.0

    def test_full(self):
        assert supply_share(30, 30) == pytest.approx(1.0)


class TestDemandShare:
    def test_basic(self):
        assert demand_share(10, 100) == pytest.approx(0.1)

    def test_zero_total(self):
        assert demand_share(5, 0) == 0.0

    def test_normalized(self):
        assert 0.0 <= demand_share(7, 20) <= 1.0


class TestGapScore:
    def test_positive_gap(self):
        """Market wants more than taught."""
        assert gap_score(0.3, 0.1) == pytest.approx(0.2)

    def test_negative_gap(self):
        """Taught more than market wants."""
        assert gap_score(0.1, 0.4) == pytest.approx(-0.3)

    def test_no_gap(self):
        assert gap_score(0.5, 0.5) == pytest.approx(0.0)


class TestCoverageAtN:
    def test_full_coverage(self):
        top5 = ["python", "sql", "ml", "stats", "tableau"]
        taught = {"python", "sql", "ml", "stats", "tableau"}
        assert coverage_at_n(top5, taught) == pytest.approx(1.0)

    def test_partial_coverage(self):
        top4 = ["python", "sql", "ml", "r"]
        taught = {"python", "r"}
        assert coverage_at_n(top4, taught) == pytest.approx(0.5)

    def test_empty_top_n(self):
        assert coverage_at_n([], {"python"}) == 0.0

    def test_no_coverage(self):
        top3 = ["spark", "scala", "kafka"]
        taught = {"python", "r"}
        assert coverage_at_n(top3, taught) == pytest.approx(0.0)
