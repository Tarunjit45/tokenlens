import json

def generate_recommendations(analysis):
    """Generates a list of recommendations based on the analysis."""
    recommendations = []
    waste_breakdown = analysis.get("waste_breakdown", {})
    
    if waste_breakdown.get("redundant_instructions", 0) > 0:
        recommendations.append(
            "Cache system prompt or use a single, consistent system prompt to avoid repetition."
        )
        
    if waste_breakdown.get("bloated_context", 0) > 0:
        recommendations.append(
            "Trim unused context. Investigate context-slimming strategies like summarization or vector search for long documents."
        )
        
    if waste_breakdown.get("oververbosity", 0) > 0:
        recommendations.append(
            "Lower 'max_tokens' for summarization and Q&A tasks. Use prompt engineering to ask for more concise answers."
        )
        
    if not recommendations:
        recommendations.append("No major sources of token waste were detected. Good job!")
        
    return recommendations

def create_report(analysis):
    """
    Creates the final JSON report.

    Args:
        analysis (dict): The analysis result from the analyzer.

    Returns:
        str: A JSON-formatted string representing the final report.
    """
    recommendations = generate_recommendations(analysis)
    
    report = {
      "total_calls": analysis.get("total_calls", 0),
      "total_tokens": analysis.get("total_tokens", 0),
      "estimated_waste_tokens": analysis.get("estimated_waste_tokens", 0),
      "waste_percentage": (
          (analysis.get("estimated_waste_tokens", 0) / analysis.get("total_tokens", 1)) * 100
      ),
      "waste_breakdown": analysis.get("waste_breakdown", {}),
      "recommendations": recommendations
    }
    
    # Clean up the report for presentation
    # Ensure waste breakdown doesn't have entries with 0 waste
    report["waste_breakdown"] = {
        k: v for k, v in report["waste_breakdown"].items() if v > 0
    }
    report["waste_percentage"] = round(report["waste_percentage"], 2)

    return json.dumps(report, indent=2)
