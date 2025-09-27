"""
LCA Data Module
Contains all the environmental impact data for different materials and lifecycle stages.
"""

# --- Simplified LCA Data Model ---
# All values are per kg
# Scores are mock data for demonstration
MATERIAL_DATA = {
    'aluminum_virgin': {'carbon': 15.0, 'water': 1.5, 'energy': 15.0, 'waste': 2.5, 'score': 45},
    'aluminum_recycled': {'carbon': 1.5, 'water': 0.1, 'energy': 1.0, 'waste': 0.2, 'score': 92},
    'copper_virgin': {'carbon': 3.5, 'water': 2.0, 'energy': 4.0, 'waste': 0.8, 'score': 60},
    'copper_recycled': {'carbon': 0.8, 'water': 0.3, 'energy': 0.8, 'waste': 0.15, 'score': 85},
    'steel_virgin': {'carbon': 2.5, 'water': 0.5, 'energy': 0.5, 'waste': 1.2, 'score': 75},
    'steel_recycled': {'carbon': 0.5, 'water': 0.1, 'energy': 0.2, 'waste': 0.1, 'score': 90},
    'zinc_virgin': {'carbon': 3.0, 'water': 1.0, 'energy': 1.5, 'waste': 0.6, 'score': 68},
    'zinc_recycled': {'carbon': 0.7, 'water': 0.2, 'energy': 0.5, 'waste': 0.1, 'score': 88},
    'nickel_virgin': {'carbon': 5.0, 'water': 2.5, 'energy': 5.5, 'waste': 1.0, 'score': 55},
    'nickel_recycled': {'carbon': 1.2, 'water': 0.4, 'energy': 1.5, 'waste': 0.2, 'score': 83},
    'tin_virgin': {'carbon': 4.0, 'water': 1.8, 'energy': 3.5, 'waste': 0.7, 'score': 62},
    'tin_recycled': {'carbon': 1.0, 'water': 0.3, 'energy': 0.9, 'waste': 0.1, 'score': 87},
    'lead_virgin': {'carbon': 4.5, 'water': 0.8, 'energy': 0.9, 'waste': 1.5, 'score': 58},
    'lead_recycled': {'carbon': 0.9, 'water': 0.15, 'energy': 0.2, 'waste': 0.1, 'score': 89},
    'gold_virgin': {'carbon': 25000.0, 'water': 3000.0, 'energy': 5000.0, 'waste': 1000.0, 'score': 20},
    'gold_recycled': {'carbon': 150.0, 'water': 50.0, 'energy': 200.0, 'waste': 10.0, 'score': 95},
    'silver_virgin': {'carbon': 12000.0, 'water': 1500.0, 'energy': 2500.0, 'waste': 500.0, 'score': 30},
    'silver_recycled': {'carbon': 70.0, 'water': 20.0, 'energy': 100.0, 'waste': 5.0, 'score': 93},
}

# --- Simplified Lifecycle Stage Data (Mock) ---
# Represents the percentage of impact from each stage
LIFECYCLE_IMPACTS = {
    'virgin': {
        'Raw Material Extraction': 60,
        'Manufacturing & Processing': 30,
        'Transportation': 5,
        'End-of-Life': 5,
    },
    'recycled': {
        'Raw Material Extraction': 10,
        'Manufacturing & Processing': 60,
        'Transportation': 10,
        'End-of-Life': 20,
    }
}

def get_material_data(material_id):
    """
    Get material data by material ID.
    
    Args:
        material_id (str): The material identifier
        
    Returns:
        dict: Material data or None if not found
    """
    return MATERIAL_DATA.get(material_id)

def get_all_materials():
    """
    Get all available materials formatted for dropdown.
    
    Returns:
        list: List of material dictionaries with 'id' and 'name'
    """
    return [{'id': k, 'name': k.replace('_', ' ').title()} for k in MATERIAL_DATA.keys()]

def get_lifecycle_data(material_type):
    """
    Get lifecycle impact data for material type.
    
    Args:
        material_type (str): Either 'virgin' or 'recycled'
        
    Returns:
        dict: Lifecycle impact percentages by stage
    """
    return LIFECYCLE_IMPACTS.get(material_type, LIFECYCLE_IMPACTS['virgin'])
