"""Create an interactive pie chart for SAGA club gender identity distribution."""

import plotly.express as px


def main() -> None:
    # Example counts by gender identity within the club
    labels = ["Male", "Female", "Non-binary", "Other"]
    counts = [7, 8, 4, 1]

    fig = px.pie(
        names=labels,
        values=counts,
        title="SAGA Club Gender Identity Distribution",
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")

    # Write the interactive chart to an HTML file
    fig.write_html("gender_pie.html", auto_open=True)


if __name__ == "__main__":
    main()
