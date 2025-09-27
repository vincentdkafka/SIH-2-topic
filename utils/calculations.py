"""
LCA Calculations Utility Module
Contains functions for calculating environmental impacts and scores.
"""

from data.lca_data import get_material_data, get_lifecycle_data

def calculate_environmental_impact(material_id, quantity):
    """
    Calculate environmental impact for given material and quantity.
    
    Args:
        material_id (str): The material identifier
        quantity (float): Quantity in kg
        
    Returns:
        dict: Environmental impact calculations
    """
    material_data = get_material_data(material_id)
    if not material_data:
        return None
    
    return {
        'carbon_footprint': material_data['carbon'] * quantity,
        'water_usage': material_data['water'] * quantity,
        'energy_consumption': material_data['energy'] * quantity,
        'waste_generation': material_data['waste'] * quantity,
        'overall_score': material_data['score']
    }

def get_score_class(score):
    """
    Get CSS class for score based on value.
    
    Args:
        score (int): Environmental score
        
    Returns:
        str: CSS class name
    """
    if score > 80:
        return "score-good"
    elif score > 60:
        return "score-medium"
    else:
        return "score-bad"

def get_material_type(material_id):
    """
    Determine if material is virgin or recycled.
    
    Args:
        material_id (str): The material identifier
        
    Returns:
        str: 'recycled' or 'virgin'
    """
    return 'recycled' if 'recycled' in material_id else 'virgin'

def find_hotspot_stage(material_type):
    """
    Find the lifecycle stage with highest impact.
    
    Args:
        material_type (str): Either 'virgin' or 'recycled'
        
    Returns:
        str: Name of the stage with highest impact
    """
    lifecycle_data = get_lifecycle_data(material_type)
    return max(lifecycle_data, key=lifecycle_data.get)

def get_comparison_scores(material_id):
    """
    Get virgin and recycled scores for comparison.
    
    Args:
        material_id (str): The material identifier
        
    Returns:
        dict: Virgin and recycled scores
    """
    # Extract base material name
    base_material = material_id.split('_')[0]
    
    virgin_material = f"{base_material}_virgin"
    recycled_material = f"{base_material}_recycled"
    
    virgin_data = get_material_data(virgin_material)
    recycled_data = get_material_data(recycled_material)
    
    return {
        'virgin_score': virgin_data['score'] if virgin_data else 0,
        'recycled_score': recycled_data['score'] if recycled_data else 0
    }

def format_material_name(material_id):
    """
    Format material ID to human-readable name.
    
    Args:
        material_id (str): The material identifier
        
    Returns:
        str: Formatted material name
    """
    return material_id.replace('_', ' ').title()
