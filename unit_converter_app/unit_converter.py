import streamlit as st
import math


# ----------------------------------------------------------------------
# Set Page Configuration
# ----------------------------------------------------------------------

st.set_page_config(
    page_title="Unit Converter | Effortless Conversions, Infinite Possibilities!",
    page_icon="♻️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------------------
# Custom CSS Styling with a Moving Background
# ------------------------------------------------------------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        @keyframes gradient {
            0% {background-position: 0% 50%}
            50% {background-position: 100% 50%}
            100% {background-position: 0% 50%}
        }
        
        .stApp {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(-45deg, #f2dfd7, #ffc, #fef9ff, #8ac926);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        
        .gradient-title {
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin: 1.5rem 0;
            animation: titleFloat 3s ease-in-out infinite;
        }
        
        @keyframes titleFloat {
            0%, 100% {transform: translateY(0)}
            50% {transform: translateY(-10px)}
        }
        
        [data-testid="stSidebar"] {
            background: rgba(255, 255, 255, 0.9) !important;
            backdrop-filter: blur(10px);
            border-radius: 0 20px 20px 0;
            box-shadow: 5px 0 15px rgba(0,0,0,0.1);
        }
        
        .stButton > button {
            background: linear-gradient(45deg, #4ee247, #4ee);
            border-radius: 12px;
            transition: all 0.3s ease;
        }
        
        .result-box {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 16px;
            padding: 2rem;
            margin: 2rem 0;
            animation: cardEnter 0.6s cubic-bezier(0.22, 1, 0.36, 1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------------------------
# App Title and Introduction
# ------------------------------------------------------------------------------
st.markdown("<h1 class='gradient-title'>♻️ Unit Converter ♻️</h1>", unsafe_allow_html=True)
st.write("Convert between units across various categories. ")
st.write("Select a category from the sidebar, enter your value, choose the units, and click Convert!")

# ------------------------------------------------------------------------------
# Conversion Functions
# ------------------------------------------------------------------------------
# Each function converts an input value from one unit to another using factors or formulas.

# Length Conversion (base unit: Meter)
def convert_length(value, from_unit, to_unit):
    factors = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852,
        "Nanometer": 1e-9
    }
    value_in_meters = value * factors[from_unit]
    return value_in_meters / factors[to_unit]

# Temperature Conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Area Conversion (base unit: Square Meter)
def convert_area(value, from_unit, to_unit):
    factors = {
        "Square Meter": 1,
        "Square Kilometer": 1e6,
        "Square Centimeter": 0.0001,
        "Square Millimeter": 1e-6,
        "Square Mile": 2.59e6,
        "Square Yard": 0.83612736,
        "Square Foot": 0.09290304,
        "Hectare": 10000,
        "Acre": 4046.86
    }
    value_in_sqm = value * factors[from_unit]
    return value_in_sqm / factors[to_unit]

# Mass Conversion (base unit: Kilogram)
def convert_mass(value, from_unit, to_unit):
    factors = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 1e-6,
        "Microgram": 1e-9,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Tonne": 1000,
        "Stone": 6.35029,
        "Imperial Ton": 1016.05,
        "US Ton": 907.185
    }
    value_in_kg = value * factors[from_unit]
    return value_in_kg / factors[to_unit]

# Data Transfer Rate Conversion (base unit: bits per second)
def convert_data_transfer_rate(value, from_unit, to_unit):
    factors = {
        "Bits per Second (bps)": 1,                         # Base unit: 1 bit per second
        "Kilobits per Second (Kbps)": 1e3,                  # 1 Kbps = 1,000 bits per second
        "Megabits per Second (Mbps)": 1e6,                  # 1 Mbps = 1,000,000 bits per second
        "Gigabits per Second (Gbps)": 1e9,                  # 1 Gbps = 1,000,000,000 bits per second
        "Terabits per Second (Tbps)": 1e12,                 # 1 Tbps = 1,000,000,000,000 bits per second
        "Kibibits per Second (Kibps)": 1024,                # 1 Kibps = 1,024 bits per second
        "Mebibits per Second (Mibps)": 1024**2,             # 1 Mibps = 1,048,576 bits per second
        "Gibibits per Second (Gibps)": 1024**3,             # 1 Gibps = 1,073,741,824 bits per second
        "Tebibits per Second (Tibps)": 1024**4,             # 1 Tibps = 1,099,511,627,776 bits per second
        "Bytes per Second (Bps)": 8,                        # 1 Byte per second = 8 bits per second
        "Kilobytes per Second (KBps)": 8e3,                 # 1 KBps = 8,000 bits per second
        "Megabytes per Second (MBps)": 8e6,                 # 1 MBps = 8,000,000 bits per second
        "Gigabytes per Second (GBps)": 8e9,                 # 1 GBps = 8,000,000,000 bits per second
        "Terabytes per Second (TBps)": 8e12                 # 1 TBps = 8,000,000,000,000 bits per second
    }
    value_in_bps = value * factors[from_unit]
    return value_in_bps / factors[to_unit]

# Digital Storage Conversion (base unit: Byte)
def convert_digital_storage(value, from_unit, to_unit):
    factors = {
        "Byte": 1,
        "Kilobyte": 1024,
        "Megabyte": 1024**2,
        "Gigabyte": 1024**3,
        "Terabyte": 1024**4
    }
    value_in_bytes = value * factors[from_unit]
    return value_in_bytes / factors[to_unit]

# Energy Conversion (base unit: Joule)
def convert_energy(value, from_unit, to_unit):
    factors = {
        "Joule (J)": 1,                              # Base unit: 1 joule
        "Kilojoule (kJ)": 1e3,                       # 1 kilojoule = 1,000 joules
        "Calorie (cal)": 4.184,                      # 1 calorie = 4.184 joules
        "Kilocalorie (kcal)": 4.184e3,               # 1 kilocalorie = 4,184 joules
        "Watt-hour (Wh)": 3.6e3,                     # 1 watt-hour = 3,600 joules
        "Kilowatt-hour (kWh)": 3.6e6,                # 1 kilowatt-hour = 3,600,000 joules
        "Electronvolt (eV)": 1.602176634e-19,        # 1 electronvolt ≈ 1.602176634e-19 joules
        "British Thermal Unit (BTU)": 1055.06,       # 1 BTU ≈ 1,055.06 joules
        "Foot-pound (ft·lb)": 1.3558179483314004,    # 1 foot-pound ≈ 1.3558179483314004 joules
    }
    value_in_joules = value * factors[from_unit]
    return value_in_joules / factors[to_unit]

# Frequency Conversion (base unit: Hertz)
def convert_frequency(value, from_unit, to_unit):
    factors = {
        "Hertz (Hz)": 1,                   # Base unit: 1 Hz
        "Kilohertz (kHz)": 1e3,             # 1 kHz = 1,000 Hz
        "Megahertz (MHz)": 1e6,             # 1 MHz = 1,000,000 Hz
        "Gigahertz (GHz)": 1e9,             # 1 GHz = 1,000,000,000 Hz
    }
    value_in_hz = value * factors[from_unit]
    return value_in_hz / factors[to_unit]

# Fuel Economy Conversion
def convert_fuel_economy(value, from_unit, to_unit):
    # Supported units: "Miles per Gallon", "L/100km", "Kilometers per Liter"
    if from_unit == to_unit:
        return value
    if from_unit == "Miles per Gallon" and to_unit == "L/100km":
        return 235.214583 / value
    if from_unit == "L/100km" and to_unit == "Miles per Gallon":
        return 235.214583 / value
    if from_unit == "Miles per Gallon" and to_unit == "Kilometers per Liter":
        return value * 0.425144
    if from_unit == "Kilometers per Liter" and to_unit == "Miles per Gallon":
        return value / 0.425144
    if from_unit == "Kilometers per Liter" and to_unit == "L/100km":
        return 100 / value
    if from_unit == "L/100km" and to_unit == "Kilometers per Liter":
        return 100 / value
    return value

# Plane Angle Conversion
def convert_plane_angle(value, from_unit, to_unit):
    # Supported units: "Degree", "Radian", "Gradian"
    if from_unit == "Degree":
        value_in_degrees = value
    elif from_unit == "Radian":
        value_in_degrees = value * (180 / math.pi)
    elif from_unit == "Gradian":
        value_in_degrees = value * 0.9
    elif from_unit == "Arcminute":
        value_in_degrees = value / 60
    elif from_unit == "Arcsecond":
        value_in_degrees = value / 3600
    elif from_unit == "Milliradian":
        value_in_degrees = value * (180 / math.pi) * 1000
    if to_unit == "Degree":
        return value_in_degrees
    elif to_unit == "Radian":
        return value_in_degrees * (math.pi / 180)
    elif to_unit == "Gradian":
        return value_in_degrees / 0.9
    elif to_unit == "Arcminute":
        return value_in_degrees * 60
    elif to_unit == "Arcsecond":
        return value_in_degrees * 3600
    elif to_unit == "Milliradian":
        return value_in_degrees * (math.pi / 180) * 1000

# Pressure Conversion (base unit: Pascal)
def convert_pressure(value, from_unit, to_unit):
    factors = {
        "Pascal": 1,
        "Kilopascal": 1000,
        "Bar": 100000,
        "Atmosphere": 101325,
        "PSI": 6894.76
    }
    value_in_pa = value * factors[from_unit]
    return value_in_pa / factors[to_unit]

# Speed Conversion (base unit: meter/second)
def convert_speed(value, from_unit, to_unit):
    factors = {
        "m/s": 1,
        "km/h": 1/3.6,
        "mph": 0.44704,
        "Knots": 0.514444
    }
    value_in_mps = value * factors[from_unit]
    return value_in_mps / factors[to_unit]

# Time Conversion (base unit: Second)
def convert_time(value, from_unit, to_unit):
    factors = {
        "Second": 1,
        "Millisecond": 1e-3,       # 1 ms = 0.001 seconds
        "Microsecond": 1e-6,       # 1 µs = 0.000001 seconds
        "Nanosecond": 1e-9,        # 1 ns = 0.000000001 seconds
        "Minute": 60,              # 1 minute = 60 seconds
        "Hour": 3600,              # 1 hour = 3600 seconds
        "Day": 86400,              # 1 day = 86400 seconds
        "Week": 604800,            # 1 week = 604800 seconds
        "Month": 2629746,          # 1 month ≈ 30.44 days ≈ 2629746 seconds (average)
        "Calendar Year": 31556952, # 1 year ≈ 365.2425 days ≈ 31,556,952 seconds
        "Decade": 315569520,       # 1 decade = 10 years
        "Century": 3155695200      # 1 century = 100 years
    }
    value_in_seconds = value * factors[from_unit]
    return value_in_seconds / factors[to_unit]

# Volume Conversion (base unit: Liter)
def convert_volume(value, from_unit, to_unit):
    factors = {
        "Liter": 1,
        "Milliliter": 0.001,
        "Cubic Meter": 1000,
        "Cubic Centimeter": 0.001,
        "US Gallon": 3.78541,
        "US Pint": 0.473176
    }
    value_in_liters = value * factors[from_unit]
    return value_in_liters / factors[to_unit]

# ------------------------------------------------------------------------------
# Dictionary for Conversion Options
# ------------------------------------------------------------------------------
conversion_options = {
    "📏 Length": {
        "function": convert_length,
        "units": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch", "Nautical Mile", "Nanometer"]
    },
    "🌡️ Temperature": {
        "function": convert_temperature,
        "units": ["Celsius", "Fahrenheit", "Kelvin"]
    },
    "🗺️ Area": {
        "function": convert_area,
        "units": ["Square Meter", "Square Kilometer", "Square Centimeter", "Square Millimeter", "Hectare", "Acre", "Square Mile", "Square Yard", "Square Foot"]
    },
    "⚖️ Mass": {
        "function": convert_mass,
        "units": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce", "Tonne", "Stone", "Imperial Ton", "US Ton"]
    },
    "📶 Data Transfer Rate": {
        "function": convert_data_transfer_rate,
        "units": ["Bits per Second (bps)", "Kilobits per Second (Kbps)", "Megabits per Second (Mbps)", "Gigabits per Second (Gbps)", "Terabits per Second (Tbps)", "Kibibits per Second (Kibps)", "Mebibits per Second (Mibps)", "Gibibits per Second (Gibps)", "Tebibits per Second (Tibps)", "Bytes per Second (Bps)", "Kilobytes per Second (KBps)", "Megabytes per Second (MBps)", "Gigabytes per Second (GBps)", "Terabytes per Second (TBps)"]
    },
    "💾 Digital Storage": {
        "function": convert_digital_storage,
        "units": ["Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"]
    },
    "⚡ Energy": {
        "function": convert_energy,
        "units": ["Joule (J)", "Kilojoule (kJ)", "Calorie (cal)",  "Kilocalorie (kcal)", "Watt-hour (Wh)", "Kilowatt-hour (kWh)","Electronvolt (eV)", "British Thermal Unit (BTU)", "Foot-pound (ft·lb)"]
    },
    "🔄 Frequency": {
        "function": convert_frequency,
        "units": ["Hertz (Hz)", "Kilohertz (kHz)", "Megahertz (MHz)", "Gigahertz (GHz)"]
    },
    "⛽ Fuel Economy": {
        "function": convert_fuel_economy,
        "units": ["Miles per Gallon", "L/100km", "Kilometers per Liter"]
    },
    "📐 Plane Angle": {
        "function": convert_plane_angle,
        "units": ["Degree", "Radian", "Gradian", "Arcminute", "Arcsecond", "Milliradian"]
    },
    "🎚️ Pressure": {
        "function": convert_pressure,
        "units": ["Pascal", "Kilopascal", "Bar", "Atmosphere", "PSI"]
    },
    "🏎️ Speed": {
        "function": convert_speed,
        "units": ["m/s", "km/h", "mph", "Knots"]
    },
    "⏳ Time": {
        "function": convert_time,
        "units": ["Second", "Millisecond", "Microsecond", "Nanosecond", "Minute", "Hour", "Day", "Week", "Month", "Calendar Year", "Decade", "Century"]
    },
    "🧪 Volume": {
        "function": convert_volume,
        "units": ["Liter", "Milliliter", "Cubic Meter", "Cubic Centimeter", "US Gallon", "US Pint"]
    }
}

# ------------------------------------------------------------------------------
# Sidebar: Category Selection
# ------------------------------------------------------------------------------
    
    # Creates a dropdown menu in the Streamlit sidebar.
    # Displays the available conversion categories.
    # Uses conversion_options.keys() to extract category names from a dictionary called conversion_options.
    # The selected category is stored in selected_category.
st.sidebar.markdown("<h2 style='text-align: center; color: black; font-size: 1.3rem;'>🔧 Select Conversion Category</h2>", unsafe_allow_html=True)
selected_category = st.sidebar.selectbox("", list(conversion_options.keys()))

    # Retrieves the conversion function associated with the selected category.
    # conversion_options[selected_category] returns a dictionary containing details about that category.
    # ["function"] extracts the specific function for performing conversions.
conv_function = conversion_options[selected_category]["function"]

    # Retrieves the list of available units for the selected conversion category.
    # This allows the user to choose input/output units when performing conversions.
units = conversion_options[selected_category]["units"]


# ------------------------------------------------------------------------------
# Main Section: Input and Conversion
# ------------------------------------------------------------------------------

    # Displays a header in the app.
    # Uses f-string formatting to show the selected category dynamically (e.g., "Length Conversion", "Time Conversion").
st.header(f"{selected_category} Conversion")

    # Creates a numeric input field where users enter the value to convert.
    # The default value is 1.0.
value = st.number_input("Enter the value", value=1.0)

    # Creates a dropdown menu for selecting the input unit.
    # The list units contains the available units for the selected category.
    # The default selection is the first unit in the list.
from_unit = st.selectbox("From Unit", units, index=0)

    # Creates another dropdown menu for selecting the target unit.
    # If there is more than one unit in units, it selects the second unit by default. Otherwise, it selects the first.
to_unit = st.selectbox("To Unit", units, index=1 if len(units) > 1 else 0)

if st.button("Convert"):
    result = conv_function(value, from_unit, to_unit).__round__(4)
    st.markdown(f"<div class='result-box'><h3>{value} {from_unit} = <span style='color: maroon;'>{result}</span> {to_unit}</h3></div>", unsafe_allow_html=True)


st.markdown("""<h4 style='text-align: center; color: #333;'>Crafted with Precision | Made by Osama bin Adnan" 🔧✨</h4>""", unsafe_allow_html=True)