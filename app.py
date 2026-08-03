# STREAMLIT GROWTH VISUALIZATION DASHBOARD AND RECOMMENDATION ENGINE 
# UNLOX'S DASHBOARD 


import logging
from typing import Dict, Any, Tuple
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("UnloxStreamlitApp")


class TelemetryIngestionMock:
    """Simulates the data lake connection pulling historical asset performance."""
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def fetch_historical_payload() -> pd.DataFrame:
        try:
            np.random.seed(42)
            n_observations = 1200
            
            topic_clusters = [
                "Career Burnout", 
                "Social Isolation", 
                "Imposter Syndrome in Tech", 
                "Financial Anxiety"
            ]
            
            dataset = pd.DataFrame({
                "asset_guid": [f"unlox_ast_{i:06d}" for i in range(n_observations)],
                "struggle_topic_cluster": np.random.choice(topic_clusters, n_observations),
                "save_to_share_ratio": np.random.exponential(scale=1.2, size=n_observations),
                "cohort_retention_rate": np.random.beta(a=2, b=5, size=n_observations),
                "organic_follower_yield": np.random.negative_binomial(n=5, p=0.05, size=n_observations),
                "video_duration_seconds": np.random.uniform(15.0, 180.0, n_observations),
                "linguistic_trigger_density": np.random.uniform(0.01, 0.18, n_observations)
            })
            
            dataset.loc[dataset['struggle_topic_cluster'] == 'Career Burnout', 'organic_follower_yield'] *= 2.5
            dataset['cohort_retention_rate'] += (dataset['save_to_share_ratio'] * 0.08)
            dataset['cohort_retention_rate'] = dataset['cohort_retention_rate'].clip(0, 1)
            
            logger.info("Successfully hydrated Streamlit cache with %d telemetry records.", n_observations)
            return dataset
            
        except Exception as e:
            logger.critical("Data hydration failed: %s. Yielding empty structural DataFrame.", e)
            return pd.DataFrame()


class PrescriptiveAnalyticsEngine:
    """Rule-based expert system for determining optimal content parameters."""
    
    @staticmethod
    def compute_strategy_vector(telemetry_df: pd.DataFrame) -> Dict[str, Any]:
        if telemetry_df.empty:
            return {}

        top_yielding_cluster = (
            telemetry_df.groupby("struggle_topic_cluster")["organic_follower_yield"]
            .median()
            .idxmax()
        )
        
        high_retention_assets = telemetry_df[telemetry_df["cohort_retention_rate"] >= 0.60]
        optimal_duration_median = high_retention_assets["video_duration_seconds"].median()
        
        target_linguistic_density = high_retention_assets["linguistic_trigger_density"].quantile(0.75)

        return {
            "primary_topic_vector": top_yielding_cluster,
            "target_duration_seconds": round(optimal_duration_median, 1),
            "caption_architecture": f"High-Density Trigger Mapping (Target >{target_linguistic_density:.1%} density)"
        }


class UnloxGrowthDashboard:
    def __init__(self):
        st.set_page_config(
            page_title="UNLOX | Audience Intelligence",
            page_icon="📈",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        self.dataset = TelemetryIngestionMock.fetch_historical_payload()

    def _render_sidebar_recommender(self) -> None:
        with st.sidebar:
            st.header("⚙️ Optimization Recommender")
            st.markdown("---")
            
            if self.dataset.empty:
                st.warning("Insufficient telemetry to generate prescriptive rules.")
                return
                
            strategy = PrescriptiveAnalyticsEngine.compute_strategy_vector(self.dataset)
            
            st.subheader("Upcoming Sprint Allocation")
            st.metric("High-Probability Topic", strategy.get("primary_topic_vector", "N/A"))
            
            st.subheader("Asset Specifications")
            st.metric("Optimal Duration (s)", strategy.get("target_duration_seconds", 0))
            
            st.subheader("Copywriting Directive")
            st.info(strategy.get("caption_architecture", "N/A"))
            
            st.markdown("---")
            st.caption("Engineered via historical top-quartile retention performance.")

    def _render_dynamic_kpis(self) -> None:
        if self.dataset.empty:
            return

        total_followers = int(self.dataset["organic_follower_yield"].sum())
        avg_sts_ratio = float(self.dataset["save_to_share_ratio"].mean())
        
        top_topic = (
            self.dataset.groupby("struggle_topic_cluster")["organic_follower_yield"]
            .sum()
            .idxmax()
        )

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Aggregate Organic Yield", f"{total_followers:,}")
            with col2:
                st.metric("Mean Save-to-Share Ratio", f"{avg_sts_ratio:.2f}")
            with col3:
                st.metric("Dominant Struggle Cluster", top_topic)
        
        st.markdown("<br>", unsafe_allow_html=True)

    def _render_visualizations(self) -> None:
        if self.dataset.empty:
            st.error("Telemetry payload empty. Awaiting upstream ingestion.")
            return

        with st.container():
            col_left, col_right = st.columns(2)
            
            with col_left:
                st.subheader("Topic Cluster vs. Organic Yield")
                fig_bar = px.box(
                    self.dataset,
                    x="struggle_topic_cluster",
                    y="organic_follower_yield",
                    color="struggle_topic_cluster",
                    template="plotly_dark",
                    labels={
                        "struggle_topic_cluster": "Psychographic Anchor",
                        "organic_follower_yield": "Follower Acquisition Rate"
                    }
                )
                fig_bar.update_layout(showlegend=False, margin=dict(t=20, b=20, l=20, r=20))
                st.plotly_chart(fig_bar, use_container_width=True)

            with col_right:
                st.subheader("Engagement Velocity vs. Retention")
                fig_scatter = px.scatter(
                    self.dataset,
                    x="save_to_share_ratio",
                    y="cohort_retention_rate",
                    color="struggle_topic_cluster",
                    opacity=0.6,
                    trendline="ols",
                    template="plotly_dark",
                    labels={
                        "save_to_share_ratio": "Save-to-Share Ratio (Velocity)",
                        "cohort_retention_rate": "30-Day Cohort Retention"
                    }
                )
                fig_scatter.update_layout(margin=dict(t=20, b=20, l=20, r=20))
                st.plotly_chart(fig_scatter, use_container_width=True)

    def execute_render_pipeline(self) -> None:
        st.title("UNLOX Audience Intelligence Platform")
        st.markdown("Real-time telemetry and prescriptive modeling for content architecture.")
        
        self._render_sidebar_recommender()
        self._render_dynamic_kpis()
        self._render_visualizations()


if __name__ == "__main__":
    app = UnloxGrowthDashboard()
    app.execute_render_pipeline()