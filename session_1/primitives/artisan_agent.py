import os
import json
import time
from session_1.primitives.shared_utils import create_azure_openai_client

# Define artisan tools for building
def use_measuring_tape(item: str, dimension: str = "all"):
    """Measure dimensions of materials"""
    measurements = {
        "wood_plank": {"length": "30cm", "width": "15cm", "thickness": "2cm"},
        "roof_piece": {"length": "20cm", "width": "20cm", "angle": "45°"},
        "entrance_hole": {"diameter": "3.2cm", "position": "center"},
        "picture_frame_wood": {"length": "40cm", "width": "5cm", "thickness": "1cm"},
        "shelf_board": {"length": "60cm", "width": "25cm", "thickness": "2cm"},
        "shelf_support": {"length": "25cm", "width": "3cm", "thickness": "3cm"}
    }
    
    result = measurements.get(item, {"measurement": "unknown"})
    return json.dumps({
        "tool": "measuring_tape",
        "item": item,
        "dimension_requested": dimension,
        "result": result,
        "status": "measured"
    })

def use_saw(material: str, cut_type: str, measurement: str):
    """Cut materials to size"""
    time.sleep(0.5)  # Simulate work time
    return json.dumps({
        "tool": "saw",
        "action": f"Cut {material} using {cut_type} cut",
        "measurement": measurement,
        "status": "completed",
        "result": f"{material} cut to {measurement}"
    })

def use_drill(material: str, hole_size: str, purpose: str):
    """Drill holes in materials"""
    time.sleep(0.5)  # Simulate work time
    return json.dumps({
        "tool": "drill",
        "action": f"Drilled {hole_size} hole in {material}",
        "purpose": purpose,
        "status": "completed"
    })

def use_hammer(nail_type: str, pieces: list, purpose: str):
    """Hammer nails to join pieces"""
    time.sleep(0.5)  # Simulate work time
    return json.dumps({
        "tool": "hammer",
        "action": f"Hammered {nail_type} to join pieces",
        "pieces_joined": pieces,
        "purpose": purpose,
        "status": "completed"
    })

def use_sandpaper(surface: str, grit: int):
    """Sand surfaces smooth"""
    time.sleep(0.5)  # Simulate work time
    return json.dumps({
        "tool": "sandpaper",
        "action": f"Sanded {surface} with {grit} grit sandpaper",
        "result": "Surface is now smooth",
        "status": "completed"
    })

def use_paint_brush(color: str, surface: str, coats: int = 1):
    """Paint surfaces"""
    time.sleep(0.5)  # Simulate work time
    return json.dumps({
        "tool": "paint_brush",
        "action": f"Applied {coats} coat(s) of {color} paint to {surface}",
        "drying_time": "2 hours",
        "status": "completed"
    })

# Define the tools schema for the artisan
artisan_tools = [
    {
        "type": "function",
        "function": {
            "name": "use_measuring_tape",
            "description": "Measure dimensions of materials before cutting or drilling",
            "parameters": {
                "type": "object",
                "properties": {
                    "item": {
                        "type": "string",
                        "description": "The item to measure (e.g., wood_plank, roof_piece, entrance_hole)"
                    },
                    "dimension": {
                        "type": "string",
                        "description": "What dimension to measure (e.g., length, width, diameter)"
                    }
                },
                "required": ["item", "dimension"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "use_saw",
            "description": "Cut wood or other materials to required size",
            "parameters": {
                "type": "object",
                "properties": {
                    "material": {
                        "type": "string",
                        "description": "The material to cut (e.g., wood plank, pine board)"
                    },
                    "cut_type": {
                        "type": "string",
                        "description": "Type of cut (e.g., straight, angled, curved)"
                    },
                    "measurement": {
                        "type": "string",
                        "description": "The measurement for the cut (e.g., 15cm, 45 degree angle)"
                    }
                },
                "required": ["material", "cut_type", "measurement"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "use_drill",
            "description": "Drill holes for screws, entrance holes, or ventilation",
            "parameters": {
                "type": "object",
                "properties": {
                    "material": {
                        "type": "string",
                        "description": "The material to drill into"
                    },
                    "hole_size": {
                        "type": "string",
                        "description": "Size of the hole (e.g., 3mm, 3.2cm)"
                    },
                    "purpose": {
                        "type": "string",
                        "description": "Purpose of the hole (e.g., entrance, screw hole, ventilation)"
                    }
                },
                "required": ["material", "hole_size", "purpose"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "use_hammer",
            "description": "Hammer nails to join pieces together",
            "parameters": {
                "type": "object",
                "properties": {
                    "nail_type": {
                        "type": "string",
                        "description": "Type of nail (e.g., finishing nail, roofing nail)"
                    },
                    "pieces": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of pieces to join"
                    },
                    "purpose": {
                        "type": "string",
                        "description": "What structure is being created"
                    }
                },
                "required": ["nail_type", "pieces", "purpose"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "use_sandpaper",
            "description": "Sand surfaces to make them smooth",
            "parameters": {
                "type": "object",
                "properties": {
                    "surface": {
                        "type": "string",
                        "description": "The surface to sand"
                    },
                    "grit": {
                        "type": "number",
                        "description": "Sandpaper grit (e.g., 120 for rough, 220 for fine)"
                    }
                },
                "required": ["surface", "grit"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "use_paint_brush",
            "description": "Paint or stain the finished product",
            "parameters": {
                "type": "object",
                "properties": {
                    "color": {
                        "type": "string",
                        "description": "Color of paint or stain"
                    },
                    "surface": {
                        "type": "string",
                        "description": "Surface to paint"
                    },
                    "coats": {
                        "type": "number",
                        "description": "Number of coats to apply"
                    }
                },
                "required": ["color", "surface"]
            }
        }
    }
]

# Map function names to actual functions and emoticons
available_tools = {
    "use_measuring_tape": use_measuring_tape,
    "use_saw": use_saw,
    "use_drill": use_drill,
    "use_hammer": use_hammer,
    "use_sandpaper": use_sandpaper,
    "use_paint_brush": use_paint_brush
}

# Emoticons for each tool
tool_emoticons = {
    "use_measuring_tape": "📏",
    "use_saw": "🪚",
    "use_drill": "⚙️",
    "use_hammer": "🔨",
    "use_sandpaper": "📜",
    "use_paint_brush": "🖌️"
}

def demonstrate_artisan_agent():
    """
    Demonstrates an AI artisan agent that uses multiple tools to build something.
    Shows decision-making loop and tool selection process.
    """
    print("\n" + "="*60)
    print("🔨 ARTISAN AGENT DEMONSTRATION")
    print("Choose a project complexity level:")
    print("="*60)
    print("1. Simple: Wooden Picture Frame (3-4 tools)")
    print("2. Medium: Small Bookshelf (5-6 tools)")
    print("3. Complex: Wooden Birdhouse (6+ tools)")
    print("="*60 + "\n")
    
    # Get user choice
    while True:
        choice = input("Select complexity (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            break
        print("Please enter 1, 2, or 3")
    
    # Define projects based on complexity
    projects = {
        "1": {
            "name": "Build a simple wooden picture frame",
            "description": "A basic 8x10 inch picture frame",
            "system_prompt": """You are an artisan AI who builds simple items step by step.
            For this simple project, focus on measuring, cutting, and joining.
            Keep it straightforward - measure, cut to size, join pieces, and apply finish."""
        },
        "2": {
            "name": "Build a small bookshelf",
            "description": "A two-tier bookshelf for desk use",
            "system_prompt": """You are an artisan AI who builds furniture step by step.
            For this medium project, you'll need to measure multiple pieces, make precise cuts,
            drill for screws, assemble carefully, sand surfaces, and apply finish.
            Plan for two shelves with proper support."""
        },
        "3": {
            "name": "Build a wooden birdhouse",
            "description": "A complete birdhouse with entrance hole and sloped roof",
            "system_prompt": """You are a master artisan AI who builds complex items step by step.
            For this complex project, you must measure all components, cut various pieces including
            angled roof pieces, drill entrance and ventilation holes, assemble walls and roof,
            sand all surfaces smooth, and paint with weather-resistant finish.
            Include proper measurements for bird entry and ensure structural integrity."""
        }
    }
    
    selected_project = projects[choice]
    
    print(f"\n🎯 Project: {selected_project['name']}")
    print(f"📝 Description: {selected_project['description']}\n")
    
    client = create_azure_openai_client()
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
    
    # Initialize the artisan's context
    messages = [
        {
            "role": "system", 
            "content": selected_project['system_prompt']
        }
    ]
    
    messages.append({"role": "user", "content": f"Please {selected_project['name']}. Think through the steps and use your tools to complete it."})
    
    print("🤔 Artisan is planning the build...\n")
    
    try:
        # Initial planning response
        response = client.chat.completions.create(
            model=deployment_name,
            messages=messages,
            tools=artisan_tools,
            tool_choice="auto",
            temperature=0.7
        )
        
        response_message = response.choices[0].message
        messages.append(response_message)
        
        # Process multiple rounds of tool usage
        step_count = 0
        # Adjust max steps based on complexity
        max_steps = {"1": 6, "2": 8, "3": 10}[choice]
        
        while step_count < max_steps:
            tool_calls = response_message.tool_calls
            
            if tool_calls:
                print(f"\n📋 Step {step_count + 1}:")
                
                for tool_call in tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    
                    # Get emoticon for the tool
                    tool_emoji = tool_emoticons.get(function_name, "🔧")
                    tool_display_name = function_name.replace('use_', '').replace('_', ' ').title()
                    
                    print(f"   {tool_emoji} Using {tool_display_name}")
                    print(f"      → {function_args}")
                    
                    # Execute the tool
                    function_to_call = available_tools[function_name]
                    function_response = function_to_call(**function_args)
                    
                    # Add tool response to messages
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response
                    })
                
                # Get next response
                response = client.chat.completions.create(
                    model=deployment_name,
                    messages=messages,
                    tools=artisan_tools,
                    tool_choice="auto",
                    temperature=0.7
                )
                
                response_message = response.choices[0].message
                messages.append(response_message)
                
                # If there's a text response, print it
                if response_message.content:
                    print(f"\n💭 Artisan: {response_message.content}")
                
                step_count += 1
            else:
                # No more tools to use, print final message
                if response_message.content:
                    print(f"\n✅ Artisan: {response_message.content}")
                    print(f"\n📊 Total steps taken: {step_count}")
                    usage = response.usage
                    print(f"📊 Tokens - Input: {usage.prompt_tokens}, Output: {usage.completion_tokens}, Total: {usage.total_tokens}")
                break
                
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*60)
    print("🏠 The artisan has demonstrated the decision-making loop!")
    print("Notice how it planned the work and selected appropriate tools")
    print("="*60)

if __name__ == "__main__":
    demonstrate_artisan_agent()