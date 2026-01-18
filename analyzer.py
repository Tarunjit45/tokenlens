from profiler import LLMCallProfiler
from heuristics import (
    detect_redundant_instructions,
    detect_bloated_context,
    detect_over_verbosity
)

def analyze_calls(call_data_list):
    """
    Analyzes a list of LLM call data for token waste.

    Args:
        call_data_list (list[dict]): A list of dictionaries, each representing an LLM call.

    Returns:
        dict: A dictionary containing the analysis results.
    """
    all_calls = [LLMCallProfiler(call) for call in call_data_list]
    
    total_tokens = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    
    # --- Waste Calculation ---
    
    # 1. Redundant Instructions (calculated across all calls)
    waste_from_instructions = detect_redundant_instructions(all_calls)
    
    # 2. Per-call waste (Bloat and Verbosity)
    waste_from_bloat = 0
    waste_from_oververbosity = 0
    
    for call in all_calls:
        total_prompt_tokens += call.prompt_tokens
        total_completion_tokens += call.completion_tokens
        
        waste_from_bloat += detect_bloated_context(call)
        waste_from_oververbosity += detect_over_verbosity(call)
        
    total_tokens = total_prompt_tokens + total_completion_tokens
    
    estimated_waste_tokens = (
        waste_from_instructions + 
        waste_from_bloat + 
        waste_from_oververbosity
    )

    analysis = {
        "total_calls": len(all_calls),
        "total_tokens": total_tokens,
        "total_prompt_tokens": total_prompt_tokens,
        "total_completion_tokens": total_completion_tokens,
        "estimated_waste_tokens": estimated_waste_tokens,
        "waste_breakdown": {
            "redundant_instructions": waste_from_instructions,
            "bloated_context": waste_from_bloat,
            "oververbosity": waste_from_oververbosity,
        },
    }
    
    return analysis
