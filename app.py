"""
Streamlit web interface for the Pharmacokinetics Calculator.

This file contains NO pharmacokinetic logic of its own. It only imports
and calls the existing, tested functions from calculator.py, and displays
the inputs/outputs in a browser UI. If you ever change the science, you
only ever need to touch calculator.py.
"""

import streamlit as st
import matplotlib.pyplot as plt

from calculator import (
    calculate_half_life,
    calculate_elimination_rate_constant,
    calculate_concentration,
    calculate_concentration_over_time,
)

st.set_page_config(page_title="PK Calculator", layout="centered")

st.title("Pharmacokinetics Calculator")
st.caption("One-compartment model, first-order elimination")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Half-life",
        "Elimination rate (k)",
        "Concentration",
        "C-t plot",
        "Semi-log plot",
    ]
)

# 1. Half-life
with tab1:
    st.subheader("Calculate Half-life")
    st.latex(r"t_{1/2} = \frac{\ln(2)}{k}")
    k = st.number_input("Elimination rate constant, k (hour⁻¹)", value=0.2, format="%.6f", key="hl_k")
    if st.button("Calculate half-life"):
        try:
            result = calculate_half_life(k)
            st.success(f"Half-life: {result:.4f} hours")
        except ValueError as e:
            st.error(str(e))

# 2. Elimination rate constant
with tab2:
    st.subheader("Calculate Elimination Rate Constant")
    st.latex(r"k = \frac{\ln(2)}{t_{1/2}}")
    half_life = st.number_input("Half-life (hours)", value=4.0, format="%.6f", key="k_half_life")
    if st.button("Calculate k"):
        try:
            result = calculate_elimination_rate_constant(half_life)
            st.success(f"Elimination rate constant (k): {result:.6f} hour⁻¹")
        except ValueError as e:
            st.error(str(e))

# 3. Concentration at a specific time
with tab3:
    st.subheader("Calculate Drug Concentration")
    st.latex(r"C(t) = C_0 \, e^{-kt}")
    c0 = st.number_input("Initial concentration, C₀", value=100.0, key="c_c0")
    k3 = st.number_input("Elimination rate constant, k (hour⁻¹)", value=0.2, format="%.6f", key="c_k")
    t3 = st.number_input("Time, t (hours)", value=5.0, key="c_t")
    if st.button("Calculate concentration"):
        try:
            result = calculate_concentration(c0, k3, t3)
            st.success(f"Concentration at t = {t3} h: {result:.4f}")
        except ValueError as e:
            st.error(str(e))

# 4. Concentration-time plot (linear)
with tab4:
    st.subheader("Concentration-Time Profile")
    c0_4 = st.number_input("Initial concentration, C₀", value=100.0, key="p_c0")
    k4 = st.number_input("Elimination rate constant, k (hour⁻¹)", value=0.2, format="%.6f", key="p_k")
    total_time_4 = st.number_input("Total time (hours)", value=24.0, min_value=0.0, key="p_total")
    if st.button("Generate plot", key="p_button"):
        try:
            if total_time_4 < 0:
                raise ValueError("Total time cannot be negative.")
            times = list(range(0, int(total_time_4) + 1))
            concentrations = calculate_concentration_over_time(c0_4, k4, times)

            fig, ax = plt.subplots()
            ax.plot(times, concentrations)
            ax.set_xlabel("Time (hours)")
            ax.set_ylabel("Drug concentration")
            ax.set_title("Concentration-Time Profile")
            ax.grid(True)
            st.pyplot(fig)
        except ValueError as e:
            st.error(str(e))

# 5. Semi-log plot
with tab5:
    st.subheader("Semi-log Concentration-Time Profile")
    c0_5 = st.number_input("Initial concentration, C₀", value=100.0, key="s_c0")
    k5 = st.number_input("Elimination rate constant, k (hour⁻¹)", value=0.2, format="%.6f", key="s_k")
    total_time_5 = st.number_input("Total time (hours)", value=24.0, min_value=0.0, key="s_total")
    if st.button("Generate semi-log plot", key="s_button"):
        try:
            if total_time_5 < 0:
                raise ValueError("Total time cannot be negative.")
            times = list(range(0, int(total_time_5) + 1))
            concentrations = calculate_concentration_over_time(c0_5, k5, times)

            fig, ax = plt.subplots()
            ax.semilogy(times, concentrations)
            ax.set_xlabel("Time (hours)")
            ax.set_ylabel("Drug concentration (log scale)")
            ax.set_title("Semi-log Concentration-Time Profile")
            ax.grid(True)
            st.pyplot(fig)
        except ValueError as e:
            st.error(str(e))
