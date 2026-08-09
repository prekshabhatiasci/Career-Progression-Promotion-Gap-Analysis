import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Career Intelligence Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PROFESSIONAL UI / CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #F5F7FA;
}

.block-container {
    max-width: 1500px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

section[data-testid="stSidebar"] {
    background-color: #17365D;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

h1, h2, h3 {
    color: #17365D;
}

div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #E4E9F0;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.07);
}

.hero {
    background-color: white;
    padding: 25px 30px;
    border-radius: 18px;
    border: 1px solid #E4E9F0;
    box-shadow: 0px 4px 16px rgba(0,0,0,0.06);
}

.hero h1 {
    margin-bottom: 5px;
}

.hero p {
    color: #555;
    font-size: 17px;
}

.stDownloadButton button {
    border-radius: 8px;
    font-weight: 600;
}

div[data-testid="stDataFrame"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD FINAL DATA
# ============================================================

@st.cache_data
def load_data():

    return pd.read_csv(
        "Final_Career_Intelligence_Output.csv"
    )


try:

    df = load_data()

except FileNotFoundError:

    st.error(
        "❌ Final_Career_Intelligence_Output.csv file nahi mili."
    )

    st.info(
        "app.py aur Final_Career_Intelligence_Output.csv "
        "same folder mein rakho."
    )

    st.stop()


# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df = df.copy()

df.columns = df.columns.str.strip()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def has_column(column):

    return column in df.columns


def unique_values(column):

    if column not in df.columns:
        return []

    return sorted(
        df[column]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )


def count_value(column, value):

    if column not in df.columns:
        return 0

    return int(
        (
            df[column]
            .astype(str)
            == str(value)
        ).sum()
    )


def mean_value(column):

    if column not in df.columns:
        return 0

    return pd.to_numeric(
        df[column],
        errors="coerce"
    ).mean()


def format_number(value, decimals=2):

    try:

        return f"{float(value):.{decimals}f}"

    except:

        return "N/A"


def make_bar_chart(
    data,
    x,
    y,
    title,
    horizontal=False
):

    if horizontal:

        fig = px.bar(
            data,
            x=y,
            y=x,
            orientation="h",
            text=y,
            title=title
        )

    else:

        fig = px.bar(
            data,
            x=x,
            y=y,
            text=y,
            title=title
        )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=30
        ),
        legend_title_text=""
    )

    return fig


# ============================================================
# FIND REAL EMPLOYEE ID COLUMN
# ============================================================

possible_id_columns = [

    "EmployeeNumber",
    "EmployeeID",
    "EmployeeId",
    "Employee ID",
    "Employee_Id",
    "ID"

]

employee_id_column = None

for column in possible_id_columns:

    if column in df.columns:

        employee_id_column = column

        break


# ============================================================
# GLOBAL KPIs
# ============================================================

total_employees = len(df)

critical_retention = count_value(
    "RetentionPriority",
    "Critical"
)

high_retention = count_value(
    "RetentionPriority",
    "High"
)

critical_promotion = count_value(
    "PromotionGapRisk",
    "Critical"
)

high_promotion = count_value(
    "PromotionGapRisk",
    "High"
)

urgent_training = count_value(
    "TrainingNeedLevel",
    "Urgent Need"
)

average_promotion_gap = mean_value(
    "PromotionGapScore"
)

average_retention = mean_value(
    "RetentionOpportunityIndex"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    "# 📊 Career"
)

st.sidebar.markdown(
    "## Intelligence"
)

st.sidebar.caption(
    "Workforce Analytics & HR Decision Support"
)

st.sidebar.markdown("---")


page = st.sidebar.radio(
    "Select Page",
    [
        "🏠 Home Dashboard",
        "🎯 Career Clustering",
        "⚠️ Risk & Retention",
        "👤 Employee Explorer"
    ]
)


st.sidebar.markdown("---")

st.sidebar.markdown(
    "### 📁 Dataset Information"
)

st.sidebar.write(
    f"Employees: **{len(df):,}**"
)

st.sidebar.write(
    f"Columns: **{len(df.columns)}**"
)

if employee_id_column:

    st.sidebar.success(
        f"Employee ID: {employee_id_column}"
    )

else:

    st.sidebar.info(
        "Employee ID column not detected"
    )


# ============================================================
# PAGE 1 — HOME DASHBOARD
# ============================================================

if page == "🏠 Home Dashboard":

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.markdown("""
    <div class="hero">

    <h1>📊 Career Intelligence Dashboard</h1>

    <p>
    Employee career growth, promotion risk,
    training needs and retention insights.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("---")


    # --------------------------------------------------------
    # WORKFORCE OVERVIEW
    # --------------------------------------------------------

    st.header(
        "📌 Workforce Overview"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Total Employees",
            f"{total_employees:,}"
        )


    with col2:

        st.metric(
            "🔴 Critical Retention",
            f"{critical_retention:,}"
        )


    with col3:

        st.metric(
            "🟠 High Promotion Risk",
            f"{high_promotion:,}"
        )


    with col4:

        st.metric(
            "🎓 Urgent Training",
            f"{urgent_training:,}"
        )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "🔴 Critical Promotion Risk",
            f"{critical_promotion:,}"
        )


    with col2:

        st.metric(
            "🟠 High Retention",
            f"{high_retention:,}"
        )


    with col3:

        st.metric(
            "📈 Avg Promotion Gap",
            format_number(
                average_promotion_gap,
                3
            )
        )


    with col4:

        st.metric(
            "💚 Avg Retention Opportunity",
            format_number(
                average_retention,
                2
            )
        )


    # --------------------------------------------------------
    # CAREER CLUSTER
    # --------------------------------------------------------

    st.markdown("---")

    st.header(
        "🎯 Career Cluster Distribution"
    )


    if has_column(
        "CareerClusterName"
    ):

        cluster_data = (
            df[
                "CareerClusterName"
            ]
            .value_counts()
            .reset_index()
        )


        cluster_data.columns = [
            "CareerClusterName",
            "Employees"
        ]


        col1, col2 = st.columns(2)


        with col1:

            fig = make_bar_chart(
                cluster_data,
                "CareerClusterName",
                "Employees",
                "Employees by Career Cluster"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        with col2:

            fig = px.pie(
                cluster_data,
                names="CareerClusterName",
                values="Employees",
                hole=0.48,
                title="Career Cluster Composition"
            )


            fig.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # --------------------------------------------------------
    # RETENTION + PROMOTION
    # --------------------------------------------------------

    st.header(
        "⚠️ Retention & Promotion"
    )


    col1, col2 = st.columns(2)


    with col1:

        if has_column(
            "RetentionPriority"
        ):

            data = (
                df[
                    "RetentionPriority"
                ]
                .value_counts()
                .reset_index()
            )


            data.columns = [
                "RetentionPriority",
                "Employees"
            ]


            fig = make_bar_chart(
                data,
                "RetentionPriority",
                "Employees",
                "Retention Priority"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    with col2:

        if has_column(
            "PromotionGapRisk"
        ):

            data = (
                df[
                    "PromotionGapRisk"
                ]
                .value_counts()
                .reset_index()
            )


            data.columns = [
                "PromotionGapRisk",
                "Employees"
            ]


            fig = make_bar_chart(
                data,
                "PromotionGapRisk",
                "Employees",
                "Promotion Gap Risk"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # --------------------------------------------------------
    # CAREER GROWTH + TRAINING
    # --------------------------------------------------------

    st.header(
        "🚀 Career Growth & Training"
    )


    col1, col2 = st.columns(2)


    with col1:

        if has_column(
            "CareerGrowthLevel"
        ):

            data = (
                df[
                    "CareerGrowthLevel"
                ]
                .value_counts()
                .reset_index()
            )


            data.columns = [
                "CareerGrowthLevel",
                "Employees"
            ]


            fig = px.pie(
                data,
                names="CareerGrowthLevel",
                values="Employees",
                hole=0.48,
                title="Career Growth Level"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    with col2:

        if has_column(
            "TrainingNeedLevel"
        ):

            data = (
                df[
                    "TrainingNeedLevel"
                ]
                .value_counts()
                .reset_index()
            )


            data.columns = [
                "TrainingNeedLevel",
                "Employees"
            ]


            fig = make_bar_chart(
                data,
                "TrainingNeedLevel",
                "Employees",
                "Training Need Distribution"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # --------------------------------------------------------
    # MANAGER STABILITY
    # --------------------------------------------------------

    if has_column(
        "ManagerStabilityImpact"
    ):

        st.header(
            "👨‍💼 Manager Stability Impact"
        )


        data = (
            df[
                "ManagerStabilityImpact"
            ]
            .value_counts()
            .reset_index()
        )


        data.columns = [
            "ManagerStabilityImpact",
            "Employees"
        ]


        fig = make_bar_chart(
            data,
            "ManagerStabilityImpact",
            "Employees",
            "Manager Stability Impact"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # HR ACTIONS
    # --------------------------------------------------------

    if has_column(
        "SuggestedAction"
    ):

        st.header(
            "💡 Recommended HR Actions"
        )


        data = (
            df[
                "SuggestedAction"
            ]
            .value_counts()
            .reset_index()
        )


        data.columns = [
            "SuggestedAction",
            "Employees"
        ]


        fig = make_bar_chart(
            data,
            "SuggestedAction",
            "Employees",
            "Recommended HR Actions",
            horizontal=True
        )


        fig.update_layout(
            height=500
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # MANAGEMENT SUMMARY
    # --------------------------------------------------------

    st.markdown("---")

    st.header(
        "💡 Management Summary"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.info(
            f"""
            **Workforce**

            {total_employees:,} employees
            are included in the analysis.
            """
        )


    with col2:

        st.warning(
            f"""
            **Retention Attention**

            {critical_retention:,} employees
            have Critical retention priority.
            """
        )


    with col3:

        st.error(
            f"""
            **Promotion Attention**

            {critical_promotion:,} employees
            have Critical promotion risk.
            """
        )


# ============================================================
# PAGE 2 — CAREER CLUSTERING
# ============================================================

elif page == "🎯 Career Clustering":

    st.title(
        "🎯 Career Clustering Analysis"
    )


    st.write(
        "Explore employee career segments "
        "and progression characteristics."
    )


    st.markdown("---")


    # --------------------------------------------------------
    # CLUSTER FILTER
    # --------------------------------------------------------

    if has_column(
        "CareerClusterName"
    ):

        cluster_options = [
            "All"
        ] + unique_values(
            "CareerClusterName"
        )


        selected_cluster = st.selectbox(
            "Select Career Cluster",
            cluster_options
        )


        if selected_cluster == "All":

            cluster_df = df.copy()

        else:

            cluster_df = df[
                df[
                    "CareerClusterName"
                ]
                .astype(str)
                ==
                selected_cluster
            ].copy()


    else:

        cluster_df = df.copy()


    # --------------------------------------------------------
    # CLUSTER KPIs
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Employees",
            f"{len(cluster_df):,}"
        )


    with col2:

        if has_column(
            "CareerGrowthScore"
        ):

            st.metric(
                "Avg Growth Score",
                format_number(
                    cluster_df[
                        "CareerGrowthScore"
                    ].mean()
                )
            )


    with col3:

        if has_column(
            "PromotionGapScore"
        ):

            st.metric(
                "Avg Promotion Gap",
                format_number(
                    cluster_df[
                        "PromotionGapScore"
                    ].mean(),
                    3
                )
            )


    with col4:

        if has_column(
            "TrainingTimesLastYear"
        ):

            st.metric(
                "Avg Training",
                format_number(
                    cluster_df[
                        "TrainingTimesLastYear"
                    ].mean()
                )
            )


    st.markdown("---")


    # --------------------------------------------------------
    # CLUSTER COMPOSITION
    # --------------------------------------------------------

    if has_column(
        "CareerClusterName"
    ):

        st.header(
            "📊 Career Cluster Composition"
        )


        data = (
            df[
                "CareerClusterName"
            ]
            .value_counts()
            .reset_index()
        )


        data.columns = [
            "CareerClusterName",
            "Employees"
        ]


        col1, col2 = st.columns(2)


        with col1:

            fig = px.pie(
                data,
                names="CareerClusterName",
                values="Employees",
                hole=0.48
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        with col2:

            fig = make_bar_chart(
                data,
                "CareerClusterName",
                "Employees",
                "Employees per Career Cluster"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


        # ----------------------------------------------------
        # CLUSTER SUMMARY TABLE
        # ----------------------------------------------------

        st.header(
            "📋 Career Cluster Summary"
        )


        summary = (
            df.groupby(
                "CareerClusterName"
            )
            .size()
            .reset_index(
                name="Employees"
            )
        )


        mappings = [

            (
                "YearsAtCompany",
                "Avg Years at Company"
            ),

            (
                "YearsInCurrentRole",
                "Avg Current Role Years"
            ),

            (
                "YearsSinceLastPromotion",
                "Avg Years Since Promotion"
            ),

            (
                "CareerGrowthScore",
                "Avg Career Growth"
            ),

            (
                "PromotionGapScore",
                "Avg Promotion Gap"
            ),

            (
                "RetentionOpportunityIndex",
                "Avg Retention Opportunity"
            )

        ]


        for source, target in mappings:

            if has_column(source):

                temp = (
                    df.groupby(
                        "CareerClusterName"
                    )[source]
                    .mean()
                    .round(2)
                    .reset_index(
                        name=target
                    )
                )


                summary = summary.merge(
                    temp,
                    on="CareerClusterName",
                    how="left"
                )


        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )


    # --------------------------------------------------------
    # CAREER GROWTH
    # --------------------------------------------------------

    if (
        has_column("CareerClusterName")
        and
        has_column("CareerGrowthScore")
    ):

        st.header(
            "🚀 Career Growth Score by Cluster"
        )


        fig = px.box(
            df,
            x="CareerClusterName",
            y="CareerGrowthScore",
            color="CareerClusterName",
            title="Career Growth Score by Career Cluster"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # PROMOTION GAP
    # --------------------------------------------------------

    if (
        has_column("CareerClusterName")
        and
        has_column("YearsSinceLastPromotion")
    ):

        st.header(
            "📈 Promotion Gap by Cluster"
        )


        fig = px.box(
            df,
            x="CareerClusterName",
            y="YearsSinceLastPromotion",
            color="CareerClusterName",
            title="Years Since Last Promotion by Cluster"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # TRAINING
    # --------------------------------------------------------

    if (
        has_column("CareerClusterName")
        and
        has_column("TrainingTimesLastYear")
    ):

        st.header(
            "🎓 Training by Cluster"
        )


        fig = px.box(
            df,
            x="CareerClusterName",
            y="TrainingTimesLastYear",
            color="CareerClusterName",
            title="Training Times Last Year by Cluster"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # ATTRITION
    # --------------------------------------------------------

    if (
        has_column("CareerClusterName")
        and
        has_column("Attrition")
    ):

        st.header(
            "⚠️ Career Cluster vs Attrition"
        )


        data = (
            df.groupby(
                [
                    "CareerClusterName",
                    "Attrition"
                ]
            )
            .size()
            .reset_index(
                name="Employees"
            )
        )


        data["Attrition"] = (
            data["Attrition"]
            .astype(str)
            .replace(
                {
                    "0": "Stayed",
                    "1": "Left",
                    "No": "Stayed",
                    "Yes": "Left"
                }
            )
        )


        fig = px.bar(
            data,
            x="CareerClusterName",
            y="Employees",
            color="Attrition",
            barmode="group",
            text="Employees",
            title="Career Cluster vs Attrition"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# PAGE 3 — RISK & RETENTION
# ============================================================

elif page == "⚠️ Risk & Retention":

    st.title(
        "⚠️ Risk & Retention Analysis"
    )


    st.write(
        "Identify employees requiring attention "
        "for promotion, training and retention."
    )


    st.markdown("---")


    # --------------------------------------------------------
    # RISK KPIs
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "🔴 Critical Retention",
            f"{critical_retention:,}"
        )


    with col2:

        st.metric(
            "🔴 Critical Promotion",
            f"{critical_promotion:,}"
        )


    with col3:

        st.metric(
            "🟠 High Promotion",
            f"{high_promotion:,}"
        )


    with col4:

        st.metric(
            "🎓 Urgent Training",
            f"{urgent_training:,}"
        )


    st.markdown("---")


    # --------------------------------------------------------
    # RISK CHARTS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        if has_column(
            "PromotionGapRisk"
        ):

            data = (
                df[
                    "PromotionGapRisk"
                ]
                .value_counts()
                .reset_index()
            )


            data.columns = [
                "Risk",
                "Employees"
            ]


            fig = make_bar_chart(
                data,
                "Risk",
                "Employees",
                "Promotion Gap Risk"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    with col2:

        if has_column(
            "RetentionPriority"
        ):

            data = (
                df[
                    "RetentionPriority"
                ]
                .value_counts()
                .reset_index()
            )


            data.columns = [
                "Priority",
                "Employees"
            ]


            fig = make_bar_chart(
                data,
                "Priority",
                "Employees",
                "Retention Priority"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # --------------------------------------------------------
    # TRAINING + MANAGER
    # --------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        if has_column(
            "TrainingNeedLevel"
        ):

            data = (
                df[
                    "TrainingNeedLevel"
                ]
                .value_counts()
                .reset_index()
            )


            data.columns = [
                "TrainingNeed",
                "Employees"
            ]


            fig = make_bar_chart(
                data,
                "TrainingNeed",
                "Employees",
                "Training Need Distribution"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    with col2:

        if has_column(
            "ManagerStabilityImpact"
        ):

            data = (
                df[
                    "ManagerStabilityImpact"
                ]
                .value_counts()
                .reset_index()
            )


            data.columns = [
                "Impact",
                "Employees"
            ]


            fig = make_bar_chart(
                data,
                "Impact",
                "Employees",
                "Manager Stability Impact"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # --------------------------------------------------------
    # HIGH PRIORITY EMPLOYEES
    # --------------------------------------------------------

    st.markdown("---")

    st.header(
        "🚨 Employees Requiring Immediate Attention"
    )


    if has_column(
        "RetentionPriority"
    ):

        retention_mask = (
            df[
                "RetentionPriority"
            ]
            .astype(str)
            .isin(
                [
                    "Critical",
                    "High"
                ]
            )
        )

    else:

        retention_mask = pd.Series(
            False,
            index=df.index
        )


    if has_column(
        "PromotionGapRisk"
    ):

        promotion_mask = (
            df[
                "PromotionGapRisk"
            ]
            .astype(str)
            .isin(
                [
                    "Critical",
                    "High"
                ]
            )
        )

    else:

        promotion_mask = pd.Series(
            False,
            index=df.index
        )


    high_priority = df[
        retention_mask
        |
        promotion_mask
    ].copy()


    if has_column(
        "RetentionOpportunityIndex"
    ):

        high_priority = (
            high_priority
            .sort_values(
                "RetentionOpportunityIndex",
                ascending=False
            )
        )


    priority_columns = [

        employee_id_column,

        "Department",
        "JobRole",
        "JobLevel",
        "YearsAtCompany",
        "YearsInCurrentRole",
        "YearsSinceLastPromotion",
        "CareerClusterName",
        "CareerGrowthScore",
        "PromotionGapScore",
        "PromotionGapRisk",
        "TrainingNeedLevel",
        "ManagerStabilityImpact",
        "RetentionOpportunityIndex",
        "RetentionPriority",
        "SuggestedAction"

    ]


    priority_columns = [

        column
        for column in priority_columns
        if column is not None
        and column in high_priority.columns

    ]


    st.dataframe(
        high_priority[
            priority_columns
        ],
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------------

    st.download_button(
        "📥 Download High-Priority Employee List",

        high_priority.to_csv(
            index=False
        ).encode("utf-8"),

        "High_Priority_Employees.csv",

        "text/csv"
    )


    # --------------------------------------------------------
    # HR ACTION
    # --------------------------------------------------------

    if has_column(
        "SuggestedAction"
    ):

        st.markdown("---")

        st.header(
            "💡 Recommended HR Actions"
        )


        data = (
            df[
                "SuggestedAction"
            ]
            .value_counts()
            .reset_index()
        )


        data.columns = [
            "SuggestedAction",
            "Employees"
        ]


        fig = make_bar_chart(
            data,
            "SuggestedAction",
            "Employees",
            "Recommended HR Actions",
            horizontal=True
        )


        fig.update_layout(
            height=550
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# PAGE 4 — EMPLOYEE EXPLORER
# ============================================================

elif page == "👤 Employee Explorer":

    st.title(
        "👤 Employee Explorer"
    )


    st.write(
        "Search, filter and inspect individual "
        "employee career intelligence."
    )


    st.markdown("---")


    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    st.header(
        "🔎 Search Employee"
    )


    if employee_id_column:

        search_value = st.text_input(
            f"Search by {employee_id_column}",
            placeholder="Enter Employee ID..."
        )

    else:

        search_value = st.text_input(
            "Search Employee",
            placeholder="Search by department, role or cluster..."
        )


    # --------------------------------------------------------
    # FILTERS
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        if has_column(
            "Department"
        ):

            department_options = [
                "All"
            ] + unique_values(
                "Department"
            )


            selected_department = st.selectbox(
                "Department",
                department_options
            )

        else:

            selected_department = "All"


    with col2:

        if has_column(
            "CareerClusterName"
        ):

            cluster_options = [
                "All"
            ] + unique_values(
                "CareerClusterName"
            )


            selected_cluster = st.selectbox(
                "Career Cluster",
                cluster_options
            )

        else:

            selected_cluster = "All"


    with col3:

        if has_column(
            "RetentionPriority"
        ):

            retention_options = [
                "All"
            ] + unique_values(
                "RetentionPriority"
            )


            selected_retention = st.selectbox(
                "Retention Priority",
                retention_options
            )

        else:

            selected_retention = "All"


    # --------------------------------------------------------
    # FILTER DATA
    # --------------------------------------------------------

    filtered_df = df.copy()


    # Search

    if search_value.strip() != "":

        search_text = (
            search_value
            .strip()
            .lower()
        )


        if employee_id_column:

            filtered_df = filtered_df[
                filtered_df[
                    employee_id_column
                ]
                .astype(str)
                .str.lower()
                .str.contains(
                    search_text,
                    na=False
                )
            ]

        else:

            searchable_columns = [

                column
                for column in [

                    "Department",
                    "JobRole",
                    "JobLevel",
                    "CareerClusterName",
                    "RetentionPriority",
                    "PromotionGapRisk"

                ]

                if column in filtered_df.columns

            ]


            mask = pd.Series(
                False,
                index=filtered_df.index
            )


            for column in searchable_columns:

                mask = (
                    mask
                    |
                    filtered_df[
                        column
                    ]
                    .astype(str)
                    .str.lower()
                    .str.contains(
                        search_text,
                        na=False
                    )
                )


            filtered_df = filtered_df[
                mask
            ]


    # Department filter

    if (
        selected_department != "All"
        and
        has_column("Department")
    ):

        filtered_df = filtered_df[
            filtered_df[
                "Department"
            ]
            .astype(str)
            ==
            selected_department
        ]


    # Cluster filter

    if (
        selected_cluster != "All"
        and
        has_column("CareerClusterName")
    ):

        filtered_df = filtered_df[
            filtered_df[
                "CareerClusterName"
            ]
            .astype(str)
            ==
            selected_cluster
        ]


    # Retention filter

    if (
        selected_retention != "All"
        and
        has_column("RetentionPriority")
    ):

        filtered_df = filtered_df[
            filtered_df[
                "RetentionPriority"
            ]
            .astype(str)
            ==
            selected_retention
        ]


    # --------------------------------------------------------
    # RESULTS
    # --------------------------------------------------------

    st.markdown("---")

    st.subheader(
        f"🔍 {len(filtered_df):,} Employee Records Found"
    )


    # --------------------------------------------------------
    # EMPLOYEE TABLE
    # --------------------------------------------------------

    table_columns = [

        employee_id_column,

        "Department",
        "JobRole",
        "JobLevel",
        "YearsAtCompany",
        "YearsInCurrentRole",
        "YearsSinceLastPromotion",
        "CareerClusterName",
        "CareerGrowthLevel",
        "CareerGrowthScore",
        "PromotionGapRisk",
        "TrainingNeedLevel",
        "RetentionPriority",
        "SuggestedAction"

    ]


    table_columns = [

        column
        for column in table_columns
        if column is not None
        and column in filtered_df.columns

    ]


    st.dataframe(
        filtered_df[
            table_columns
        ],
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # DOWNLOAD FILTERED DATA
    # --------------------------------------------------------

    st.download_button(
        "📥 Download Filtered Employee Data",

        filtered_df.to_csv(
            index=False
        ).encode("utf-8"),

        "Filtered_Employee_Data.csv",

        "text/csv"
    )


    # --------------------------------------------------------
    # EMPLOYEE PROFILE
    # --------------------------------------------------------

    if len(filtered_df) > 0:

        st.markdown("---")

        st.header(
            "👤 Employee Career Profile"
        )


        # ----------------------------------------------------
        # SELECT EMPLOYEE
        # ----------------------------------------------------

        if employee_id_column:

            employee_options = (
                filtered_df[
                    employee_id_column
                ]
                .astype(str)
                .tolist()
            )


            selected_employee = st.selectbox(
                f"Select {employee_id_column}",
                employee_options
            )


            employee = filtered_df[
                filtered_df[
                    employee_id_column
                ]
                .astype(str)
                ==
                selected_employee
            ].iloc[0]


        else:

            employee_index = st.selectbox(
                "Select Employee Record",
                filtered_df.index.tolist()
            )


            employee = filtered_df.loc[
                employee_index
            ]


        # ----------------------------------------------------
        # BASIC INFORMATION
        # ----------------------------------------------------

        st.subheader(
            "📋 Employee Information"
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            if "Department" in employee.index:

                st.metric(
                    "Department",
                    str(
                        employee[
                            "Department"
                        ]
                    )
                )


        with col2:

            if "JobRole" in employee.index:

                st.metric(
                    "Job Role",
                    str(
                        employee[
                            "JobRole"
                        ]
                    )
                )


        with col3:

            if "JobLevel" in employee.index:

                st.metric(
                    "Job Level",
                    str(
                        employee[
                            "JobLevel"
                        ]
                    )
                )


        with col4:

            if "CareerClusterName" in employee.index:

                st.metric(
                    "Career Cluster",
                    str(
                        employee[
                            "CareerClusterName"
                        ]
                    )
                )


        # ----------------------------------------------------
        # CAREER PROGRESSION
        # ----------------------------------------------------

        st.subheader(
            "📈 Career Progression"
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            if "YearsAtCompany" in employee.index:

                st.metric(
                    "Years at Company",
                    employee[
                        "YearsAtCompany"
                    ]
                )


        with col2:

            if "YearsInCurrentRole" in employee.index:

                st.metric(
                    "Current Role Years",
                    employee[
                        "YearsInCurrentRole"
                    ]
                )


        with col3:

            if "YearsSinceLastPromotion" in employee.index:

                st.metric(
                    "Years Since Promotion",
                    employee[
                        "YearsSinceLastPromotion"
                    ]
                )


        with col4:

            if "TrainingTimesLastYear" in employee.index:

                st.metric(
                    "Training Last Year",
                    employee[
                        "TrainingTimesLastYear"
                    ]
                )


        # ----------------------------------------------------
        # CAREER INTELLIGENCE
        # ----------------------------------------------------

        st.subheader(
            "🎯 Career Intelligence"
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            if "CareerGrowthScore" in employee.index:

                st.metric(
                    "Career Growth Score",
                    format_number(
                        employee[
                            "CareerGrowthScore"
                        ]
                    )
                )


        with col2:

            if "PromotionGapScore" in employee.index:

                st.metric(
                    "Promotion Gap Score",
                    format_number(
                        employee[
                            "PromotionGapScore"
                        ],
                        3
                    )
                )


        with col3:

            if "RetentionOpportunityIndex" in employee.index:

                st.metric(
                    "Retention Opportunity",
                    format_number(
                        employee[
                            "RetentionOpportunityIndex"
                        ]
                    )
                )


        with col4:

            if "PromotionGapRisk" in employee.index:

                st.metric(
                    "Promotion Risk",
                    str(
                        employee[
                            "PromotionGapRisk"
                        ]
                    )
                )


        # ----------------------------------------------------
        # RISK INDICATORS
        # ----------------------------------------------------

        st.subheader(
            "⚠️ Risk & Retention Indicators"
        )


        risk_fields = [

            (
                "Promotion Gap Risk",
                "PromotionGapRisk"
            ),

            (
                "Promotion Gap Score",
                "PromotionGapScore"
            ),

            (
                "Career Growth Level",
                "CareerGrowthLevel"
            ),

            (
                "Training Need",
                "TrainingNeedLevel"
            ),

            (
                "Manager Stability Impact",
                "ManagerStabilityImpact"
            ),

            (
                "Retention Opportunity",
                "RetentionOpportunityIndex"
            ),

            (
                "Retention Priority",
                "RetentionPriority"
            )

        ]


        risk_rows = []


        for label, column in risk_fields:

            if column in employee.index:

                risk_rows.append(
                    {
                        "Indicator": label,
                        "Value": employee[
                            column
                        ]
                    }
                )


        if risk_rows:

            risk_df = pd.DataFrame(
                risk_rows
            )


            st.dataframe(
                risk_df,
                use_container_width=True,
                hide_index=True
            )


        # ----------------------------------------------------
        # RECOMMENDED ACTION
        # ----------------------------------------------------

        if "SuggestedAction" in employee.index:

            st.subheader(
                "💡 Recommended HR Action"
            )


            st.success(
                str(
                    employee[
                        "SuggestedAction"
                    ]
                )
            )


        # ----------------------------------------------------
        # CAREER METRICS CHART
        # ----------------------------------------------------

        career_metrics = []


        metric_fields = [

            (
                "Years at Company",
                "YearsAtCompany"
            ),

            (
                "Current Role Years",
                "YearsInCurrentRole"
            ),

            (
                "Years Since Promotion",
                "YearsSinceLastPromotion"
            ),

            (
                "Training Last Year",
                "TrainingTimesLastYear"
            )

        ]


        for label, column in metric_fields:

            if column in employee.index:

                value = pd.to_numeric(
                    employee[
                        column
                    ],
                    errors="coerce"
                )


                if pd.notna(value):

                    career_metrics.append(
                        {
                            "Metric": label,
                            "Value": float(value)
                        }
                    )


        if career_metrics:

            st.subheader(
                "📊 Employee Career Metrics"
            )


            chart_df = pd.DataFrame(
                career_metrics
            )


            fig = px.bar(
                chart_df,
                x="Metric",
                y="Value",
                text="Value",
                title="Employee Career Metrics"
            )


            fig.update_traces(
                textposition="outside"
            )


            fig.update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white",
                xaxis_tickangle=-25
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    else:

        st.warning(
            "No employee records match the selected filters."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Career Intelligence Dashboard • "
    "Data Analytics & HR Decision Support"
)