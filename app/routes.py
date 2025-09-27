"""
Flask Routes Module
Contains all the route handlers for the LCA application.
"""

from flask import Blueprint, request, render_template, flash, redirect, url_for
from data.lca_data import get_all_materials, get_lifecycle_data
from utils.calculations import (
    calculate_environmental_impact,
    get_score_class,
    get_material_type,
    find_hotspot_stage,
    get_comparison_scores,
    format_material_name
)

# Create blueprint
main_bp = Blueprint('main', __name__)

# History storage (in-memory for the prototype)
history = []

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route handler for both displaying the form and processing results.
    """
    if request.method == 'POST':
        try:
            material = request.form['material']
            quantity = float(request.form['quantity'])
            
            # Calculate environmental impact
            impact_data = calculate_environmental_impact(material, quantity)
            if impact_data is None:
                flash("Error: Material not found.", "error")
                return redirect(url_for('main.index'))
            
            # Get material type and lifecycle data
            material_type = get_material_type(material)
            lifecycle_data = get_lifecycle_data(material_type)
            
            # Find hotspot stage
            hotspot_stage = find_hotspot_stage(material_type)
            
            # Get comparison scores
            comparison_scores = get_comparison_scores(material)
            
            # Format material name
            material_name = format_material_name(material)
            
            # Get score class for styling
            overall_score_class = get_score_class(impact_data['overall_score'])
            
            # Save to history
            history.append({
                'material_name': material_name,
                'quantity': quantity,
                'overall_score': impact_data['overall_score'],
            })
            
            # Render results template
            return render_template(
                'results.html',
                material_name=material_name,
                quantity=quantity,
                carbon=f"{impact_data['carbon_footprint']:.2f}",
                water=f"{impact_data['water_usage']:.2f}",
                energy=f"{impact_data['energy_consumption']:.2f}",
                overall_score=impact_data['overall_score'],
                overall_score_class=overall_score_class,
                lifecycle_data=lifecycle_data,
                hotspot_stage=hotspot_stage,
                virgin_score=comparison_scores['virgin_score'],
                recycled_score=comparison_scores['recycled_score'],
            )
            
        except ValueError:
            flash("Error: Please enter a valid quantity.", "error")
            return redirect(url_for('main.index'))
        except Exception as e:
            flash(f"An error occurred: {e}", "error")
            return redirect(url_for('main.index'))
    
    # GET request - show the form
    materials = get_all_materials()
    return render_template('index.html', materials=materials, history=history)

@main_bp.route('/health')
def health_check():
    """
    Simple health check endpoint for deployment monitoring.
    """
    return {"status": "healthy", "service": "LCA Analysis Tool"}, 200
