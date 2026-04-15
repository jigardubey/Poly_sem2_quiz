import streamlit as st
import random
import time

# Page Configuration
st.set_page_config(page_title="Polytechnic Quiz 2026", page_icon="🎓")

# --- DATABASE ---
if 'db' not in st.session_state:
    st.session_state.db = [ 
    ["Physics", "Unit 1: Wave Motion", "SHM ka displacement equation kya hai?", "y = a sin wt", "y = mc2,y = a sin wt,v = u + at,F = ma"],
    ["Physics", "Unit 1: Wave Motion", "Ultrasonic waves ki frequency kitni hoti hai?", "> 20,000 Hz", "< 20 Hz,20-20,000 Hz,> 20,000 Hz,None"],
    ["Physics", "Unit 1: Wave Motion", "Sound waves kaisa wave motion dikhati hain?", "Longitudinal", "Transverse,Longitudinal,Electromagnetic,None"],
    ["Physics", "Unit 1: Wave Motion", "Wave velocity (v), frequency (n) aur wavelength (L) ka rishta?", "v = nL", "v = n/L,v = L/n,v = nL,None"],
    ["Physics", "Unit 1: Wave Motion", "SHM mein acceleration kiske proportional hota hai?", "- Displacement", "- Velocity,- Displacement,Mass,Time"],
    ["Physics", "Unit 1: Wave Motion", "Ek complete vibration mein laga samay?", "Time Period", "Frequency,Time Period,Wavelength,Phase"],
    ["Physics", "Unit 1: Wave Motion", "Frequency ki unit kya hai?", "Hertz", "Watt,Hertz,Joule,Newton"],
    ["Physics", "Unit 1: Wave Motion", "Light waves kis tarah ki waves hain?", "Transverse", "Longitudinal,Transverse,Sound,None"],
    ["Physics", "Unit 1: Wave Motion", "Echo sunne ke liye minimum distance?", "17.2 meters", "10 meters,17.2 meters,50 meters,100 meters"],
    ["Physics", "Unit 1: Wave Motion", "Amplitude ka matlab kya hai?", "Maximum displacement", "Minimum displacement,Maximum displacement,Zero velocity,None"],
    ["Physics", "Unit 2: Optics", "TIR ka full form?", "Total Internal Reflection", "Total Inner Ray,Total Internal Reflection,Top Index,None"],
    ["Physics", "Unit 2: Optics", "Heere (Diamond) ka chamakna kiske karan hai?", "TIR", "Refraction,Reflection,TIR,Interference"],
    ["Physics", "Unit 2: Optics", "Snell's Law ka formula?", "sin i / sin r = n", "sin i * sin r = n,sin i / sin r = n,i = r,None"],
    ["Physics", "Unit 2: Optics", "Optical Fiber kis principle par kaam karta hai?", "TIR", "Refraction,Scattering,TIR,Diffraction"],
    ["Physics", "Unit 2: Optics", "Lens ki power ki unit?", "Dioptre", "Watt,Dioptre,Candela,Lux"],
    ["Physics", "Unit 2: Optics", "Critical angle par refraction angle kitna hota hai?", "90 degree", "0 degree,45 degree,90 degree,180 degree"],
    ["Physics", "Unit 2: Optics", "Convex lens kaisa lens hai?", "Converging", "Diverging,Converging,Plain,None"],
    ["Physics", "Unit 2: Optics", "Dual nature of light ka matlab?", "Wave and Particle", "Ray and Wave,Wave and Particle,Solid and Liquid,None"],
    ["Physics", "Unit 2: Optics", "Aakash ka neela rang kiske karan hota hai?", "Scattering", "Refraction,Reflection,Scattering,TIR"],
    ["Physics", "Unit 2: Optics", "Rainbow banne ka karan?", "Dispersion", "Reflection,Dispersion,Diffraction,None"],
    ["Physics", "Unit 3: Electrostatics", "Charge ki SI unit kya hai?", "Coulomb", "Volt,Ampere,Coulomb,Ohm"],
    ["Physics", "Unit 3: Electrostatics", "Coulomb's Law kiske beech force batata hai?", "Two charges", "Two masses,Two charges,Two magnets,None"],
    ["Physics", "Unit 3: Electrostatics", "Electric field ki intensity unit?", "Newton/Coulomb", "Volt/Meter,Newton/Coulomb,Both,None"],
    ["Physics", "Unit 3: Electrostatics", "Capacitance ki unit?", "Farad", "Henry,Farad,Ohm,Watt"],
    ["Physics", "Unit 3: Electrostatics", "Insulator ka dielectric constant (K) hamesha?", "> 1", "Zero,1,> 1,< 1"],
    ["Physics", "Unit 3: Electrostatics", "Gauss Law kisse juda hai?", "Electric Flux", "Magnetic Flux,Electric Flux,Current,Mass"],
    ["Physics", "Unit 3: Electrostatics", "Capacitors ko series mein jodne par formula?", "1/C = 1/C1 + 1/C2", "C = C1 + C2,1/C = 1/C1 + 1/C2,C = V/Q,None"],
    ["Physics", "Unit 3: Electrostatics", "Electric Potential kaisa quantity hai?", "Scalar", "Vector,Scalar,Tensor,None"],
    ["Physics", "Unit 3: Electrostatics", "Earth ka potential kitna mana jata hai?", "Zero", "Infinite,Zero,100V,1V"],
    ["Physics", "Unit 3: Electrostatics", "Parallel plate capacitor ki capacity badhane ke liye?", "Area badhana", "Distance badhana,Area badhana,Charge ghatana,None"],
    ["Physics", "Unit 4: Current Electricity", "Ohm's Law formula?", "V = IR", "V = I/R,P = VI,V = IR,R = V/I"],
    ["Physics", "Unit 4: Current Electricity", "Specific Resistance kiske upar depend karta hai?", "Material", "Length,Area,Material,None"],
    ["Physics", "Unit 4: Current Electricity", "Wheatstone Bridge kya maapne ke liye hai?", "Unknown Resistance", "Current,Voltage,Unknown Resistance,Power"],
    ["Physics", "Unit 4: Current Electricity", "Kirchhoff's 1st Law (KCL) conservation of?", "Charge", "Energy,Mass,Charge,Momentum"],
    ["Physics", "Unit 4: Current Electricity", "Kirchhoff's 2nd Law (KVL) conservation of?", "Energy", "Energy,Mass,Charge,None"],
    ["Physics", "Unit 4: Current Electricity", "Superconductor ka resistance?", "Zero", "Infinite,Zero,Very High,None"],
    ["Physics", "Unit 4: Current Electricity", "Resistance ki unit?", "Ohm", "Ohm,Watt,Volt,Farad"],
    ["Physics", "Unit 4: Current Electricity", "Potentiometer kya maapta hai?", "EMF", "Current,Resistance,EMF,None"],
    ["Physics", "Unit 4: Current Electricity", "Semiconductor ka temperature badhane par resistance?", "Ghat-ta hai", "Badhta hai,Ghat-ta hai,Same rehta hai,None"],
    ["Physics", "Unit 4: Current Electricity", "Meter Bridge kis par based hai?", "Wheatstone Bridge", "Ohm's Law,Wheatstone Bridge,Faraday Law,None"],
    ["Physics", "Unit 5: Magnetism", "Magnetic Flux ki unit?", "Weber", "Tesla,Weber,Henry,Ampere"],
    ["Physics", "Unit 5: Magnetism", "Flux Density ki unit?", "Tesla", "Weber,Tesla,Farad,None"],
    ["Physics", "Unit 5: Magnetism", "Magnetic field ki direction kis rule se milti hai?", "Right Hand Thumb Rule", "Lenz Law,Right Hand Thumb Rule,Ohm Law,None"],
    ["Physics", "Unit 5: Magnetism", "Paramagnetic material ka example?", "Aluminium", "Iron,Aluminium,Water,Copper"],
    ["Physics", "Unit 5: Magnetism", "Ferromagnetic material ka example?", "Iron", "Iron,Aluminium,Glass,Gold"],
    ["Physics", "Unit 5: Magnetism", "Lorentz Force formula?", "F = q(v x B)", "F = ma,F = q(v x B),F = mgh,None"],
    ["Physics", "Unit 5: Magnetism", "Magnet ke poles ko alag kiya ja sakta hai?", "Nahi", "Haan,Nahi,Sirf garam karke,None"],
    ["Physics", "Unit 5: Magnetism", "Lenz's Law kiske conservation par hai?", "Energy", "Mass,Charge,Energy,Momentum"],
    ["Physics", "Unit 5: Magnetism", "Electromagnet banane ke liye kya use hota hai?", "Soft Iron", "Steel,Soft Iron,Copper,Aluminium"],
    ["Physics", "Unit 5: Magnetism", "Earth ke magnetic poles पर dip angle?", "90 degree", "0 degree,45 degree,90 degree,180 degree"],
    ["Physics", "Unit 6: Modern Physics", "Photoelectric effect kisne explain kiya?", "Einstein", "Newton,Einstein,Bohr,Tesla"],
    ["Physics", "Unit 6: Modern Physics", "LASER ka full form mein 'S' kya hai?", "Stimulated", "Simple,Stimulated,Static,Strong"],
    ["Physics", "Unit 6: Modern Physics", "Atom ka central part kya hai?", "Nucleus", "Electron,Nucleus,Proton,None"],
    ["Physics", "Unit 6: Modern Physics", "Semiconductor mein 'Hole' kaisa charge hai?", "Positive", "Negative,Positive,Neutral,None"],
    ["Physics", "Unit 6: Modern Physics", "Solar cell kya karta hai?", "Light to Elec", "Heat to Elec,Light to Elec,Elec to Mech,None"],
    ["Physics", "Unit 6: Modern Physics", "X-rays ki khoj kisne ki?", "Roentgen", "Einstein,Roentgen,Newton,Curie"],
    ["Physics", "Unit 6: Modern Physics", "Bohr model kiske liye hai?", "Hydrogen atom", "Iron,Gold,Hydrogen atom,None"],
    ["Physics", "Unit 6: Modern Physics", "P-N junction diode ka use?", "Rectifier", "Amplifier,Rectifier,Oscillator,None"],
    ["Physics", "Unit 6: Modern Physics", "Fiber optics mein signal kaise jata hai?", "Light", "Electricity,Sound,Light,None"],
    ["Physics", "Unit 6: Modern Physics", "Nano-technology ka scale?", "10^-9 m", "10^-6 m,10^-9 m,10^-12 m,None"],
    ["Physics", "Unit 7: Misc", "Power ki unit?", "Watt", "Joule,Watt,Newton,Volt"],
    ["Physics", "Unit 7: Misc", "1 Horse Power (HP) kitne watt?", "746 W", "500 W,746 W,1000 W,750 W"],
    ["Physics", "Unit 7: Misc", "Sound ki loudness unit?", "Decibel", "Hertz,Decibel,Meter,None"],
    ["Physics", "Unit 7: Misc", "Newton's 1st law ko kya kehte hain?", "Law of Inertia", "Law of Gravity,Law of Inertia,Law of Force,None"],
    ["Physics", "Unit 7: Misc", "Gravity (g) ki value poles par?", "Maximum", "Minimum,Maximum,Zero,None"],
    ["Physics", "Unit 7: Misc", "Viscosity kisme hoti hai?", "Fluids", "Solids,Fluids,Vacuum,None"],
    ["Physics", "Unit 7: Misc", "Bernoulli's theorem kiske liye hai?", "Liquid flow", "Static liquid,Liquid flow,Solid,None"],
    ["Physics", "Unit 7: Misc", "Absolute zero temperature?", "-273.15 C", "0 C,-273.15 C,100 C,None"],
    ["Physics", "Unit 7: Misc", "Conduction kisme hota hai?", "Solids", "Solids,Liquids,Gases,Vacuum"],
    ["Physics", "Unit 7: Misc", "Radiation ke liye medium chahiye?", "Nahi", "Haan,Nahi,Sirf hawa,None"],
    ["FEEE", "Unit 1: Components", "Active component kaunsa hai?", "Transistor", "Resistor,Capacitor,Inductor,Transistor"],
    ["FEEE", "Unit 1: Components", "Passive component kaunsa hai?", "Capacitor", "Diode,Transistor,Capacitor,BJT"],
    ["FEEE", "Unit 1: Components", "Resistor kya maapta hai?", "Resistance", "Voltage,Current,Resistance,Power"],
    ["FEEE", "Unit 1: Components", "Capacitor kya store karta hai?", "Electric Charge", "Magnetic Field,Electric Charge,Heat,None"],
    ["FEEE", "Unit 1: Components", "Inductor ki unit kya hai?", "Henry", "Farad,Henry,Ohm,Tesla"],
    ["FEEE", "Unit 1: Components", "Semiconductor material kaunsa hai?", "Silicon", "Copper,Iron,Silicon,Aluminium"],
    ["FEEE", "Unit 1: Components", "P-type semiconductor mein kya zyada hote hain?", "Holes", "Electrons,Holes,Neutrons,Protons"],
    ["FEEE", "Unit 1: Components", "Diode current ko kitni disha mein bhejta hai?", "One", "One,Two,Both,None"],
    ["FEEE", "Unit 1: Components", "PN Junction forward bias mein kaise kaam karta hai?", "Closed Switch", "Open Switch,Closed Switch,Insulator,None"],
    ["FEEE", "Unit 1: Components", "Zener Diode ka use kya hai?", "Voltage Regulator", "Rectifier,Amplifier,Voltage Regulator,Filter"],
    ["FEEE", "Unit 1: Components", "BJT ka full form?", "Bipolar Junction Transistor", "Binary Junction,Bipolar Junction Transistor,Basic Junction,None"],
    ["FEEE", "Unit 1: Components", "FET kaisa device hai?", "Voltage Controlled", "Current Controlled,Voltage Controlled,Manual,None"],
    ["FEEE", "Unit 1: Components", "MOSFET ka full form?", "Metal Oxide Semiconductor FET", "Metal Open,Metal Oxide Semiconductor FET,Main Oxide,None"],
    ["FEEE", "Unit 1: Components", "Insulator ka example kya hai?", "Glass", "Copper,Gold,Glass,Silver"],
    ["FEEE", "Unit 1: Components", "LED ka full form?", "Light Emitting Diode", "Light End,Low Energy,Light Emitting Diode,None"],
    ["FEEE", "Unit 1: Components", "Transformer kaisa device hai?", "Static", "Rotating,Static,Moving,None"],
    ["FEEE", "Unit 1: Components", "Resistance kiske proportional hota hai?", "Length", "Area,Length,Width,None"],
    ["FEEE", "Unit 1: Components", "Conductance ki unit?", "Siemens", "Ohm,Siemens,Henry,Watt"],
    ["FEEE", "Unit 1: Components", "N-type mein majority carrier kya hote hain?", "Electrons", "Holes,Electrons,Ions,None"],
    ["FEEE", "Unit 1: Components", "Color coding mein 'Black' ka value?", "0", "0,1,2,3"],
    ["FEEE", "Unit 2: Instruments", "Current maapne wala instrument?", "Ammeter", "Voltmeter,Ammeter,Wattmeter,Multimeter"],
    ["FEEE", "Unit 2: Instruments", "Voltmeter kaise connect hota hai?", "Parallel", "Series,Parallel,Diagonal,None"],
    ["FEEE", "Unit 2: Instruments", "Ideal Ammeter ka resistance?", "Zero", "Zero,Infinite,High,Low"],
    ["FEEE", "Unit 2: Instruments", "Ideal Voltmeter ka resistance?", "Infinite", "Zero,Infinite,Low,Medium"],
    ["FEEE", "Unit 2: Instruments", "Wattmeter kya maapta hai?", "Power", "Current,Voltage,Power,Frequency"],
    ["FEEE", "Unit 2: Instruments", "Multimeter se kya nahi maap sakte?", "Frequency", "Voltage,Current,Resistance,Frequency"],
    ["FEEE", "Unit 2: Instruments", "CRO ka full form?", "Cathode Ray Oscilloscope", "Cathode Ray Oscilloscope,Common Radio,Current Ray,None"],
    ["FEEE", "Unit 2: Instruments", "CRO ki screen par kya dikhta hai?", "Waveform", "Digits,Waveform,Light,Sound"],
    ["FEEE", "Unit 2: Instruments", "Frequency ki unit?", "Hertz", "Hertz,Volt,Ampere,Watt"],
    ["FEEE", "Unit 2: Instruments", "DMM ka matlab?", "Digital Multimeter", "Direct Multi,Digital Multimeter,Data Multi,None"],
    ["FEEE", "Unit 2: Instruments", "CRO mein 'Time Base' generator kahan hota hai?", "Horizontal", "Vertical,Horizontal,Trigger,None"],
    ["FEEE", "Unit 2: Instruments", "Shunt ka use kahan hota hai?", "Ammeter", "Voltmeter,Ammeter,Galvanometer,None"],
    ["FEEE", "Unit 2: Instruments", "Ohm-meter kya maapta hai?", "Resistance", "Voltage,Resistance,Power,None"],
    ["FEEE", "Unit 2: Instruments", "Megger ka use kya hai?", "High Resistance", "Low Resistance,High Resistance,Voltage,None"],
    ["FEEE", "Unit 2: Instruments", "Calibration ka matlab?", "Accuracy check", "New design,Accuracy check,Repair,None"],
    ["FEEE", "Unit 2: Instruments", "Parallax error kis mein hota hai?", "Analog Meter", "Digital Meter,Analog Meter,CRO,None"],
    ["FEEE", "Unit 2: Instruments", "Galvanometer ko Ammeter kaise banayein?", "Low Resistance in Parallel", "High Resistance,Low Resistance in Parallel,Series,None"],
    ["FEEE", "Unit 2: Instruments", "Resolution ka matlab?", "Chhota badlav maapna", "Zyada voltage,Chhota badlav maapna,Speed,None"],
    ["FEEE", "Unit 2: Instruments", "Moving Iron meter kis par kaam karta hai?", "AC and DC", "Sirf AC,Sirf DC,AC and DC,None"],
    ["FEEE", "Unit 2: Instruments", "Sensitivity ki unit?", "Ohm/Volt", "Volt/Ohm,Ohm/Volt,Ampere,None"],
    ["FEEE", "Unit 3: Digital", "Binary ka base kya hai?", "2", "10,8,2,16"],
    ["FEEE", "Unit 3: Digital", "Decimal ka base kya hai?", "10", "2,10,8,16"],
    ["FEEE", "Unit 3: Digital", "AND Gate ka output 1 kab hota hai?", "All inputs 1", "One input 1,All inputs 1,All inputs 0,None"],
    ["FEEE", "Unit 3: Digital", "NOT Gate ka dusra naam?", "Inverter", "Adder,Inverter,Multiplier,Divider"],
    ["FEEE", "Unit 3: Digital", "OR Gate kya karta hai?", "Addition", "Multiplication,Addition,Inversion,None"],
    ["FEEE", "Unit 3: Digital", "NAND Gate kiska combination hai?", "AND + NOT", "OR + NOT,AND + NOT,AND + OR,None"],
    ["FEEE", "Unit 3: Digital", "Binary '10' ka decimal value?", "2", "1,2,3,4"],
    ["FEEE", "Unit 3: Digital", "Universal Gate kaunsa hai?", "NOR", "AND,OR,NOR,XOR"],
    ["FEEE", "Unit 3: Digital", "XOR Gate ka use?", "Parity Checker", "Adder,Parity Checker,Inverter,None"],
    ["FEEE", "Unit 3: Digital", "1 Byte mein kitne Bits hote hain?", "8", "4,8,16,32"],
    ["FEEE", "Unit 3: Digital", "Hexadecimal mein 'A' ki value?", "10", "9,10,11,12"],
    ["FEEE", "Unit 3: Digital", "Octal system ka base?", "8", "2,8,10,16"],
    ["FEEE", "Unit 3: Digital", "Digital signal ki states?", "0 and 1", "0 to 9,0 and 1,Continuous,None"],
    ["FEEE", "Unit 3: Digital", "Boolean Algebra mein 1 + 1?", "1", "1,2,0,10"],
    ["FEEE", "Unit 3: Digital", "Flip-Flop kya store karta hai?", "1 Bit", "1 Byte,1 Bit,1 Word,None"],
    ["FEEE", "Unit 3: Digital", "De-Morgan's Law kahan use hota hai?", "Simplification", "Integration,Simplification,Addition,None"],
    ["FEEE", "Unit 3: Digital", "Truth Table kya dikhati hai?", "Logic States", "Voltage,Logic States,Current,None"],
    ["FEEE", "Unit 3: Digital", "Analog signal kaisa hota hai?", "Continuous", "Discrete,Continuous,Square,None"],
    ["FEEE", "Unit 3: Digital", "Most common logic level?", "TTL", "MOS,TTL,ECL,None"],
    ["FEEE", "Unit 3: Digital", "LSB ka full form?", "Least Significant Bit", "Low Super Bit,Least Significant Bit,Long Side Bit"],
    ["FEEE", "Unit 4: Magnetic", "Flux ki unit?", "Weber", "Tesla,Weber,Henry,Ampere"],
    ["FEEE", "Unit 4: Magnetic", "Flux Density ki unit?", "Tesla", "Weber,Tesla,Farad,None"],
    ["FEEE", "Unit 4: Magnetic", "Ohm's Law formula?", "V = IR", "V = I/R,P = VI,V = IR,R = V/I"],
    ["FEEE", "Unit 4: Magnetic", "Kirchhoff's Current Law (KCL)?", "Sum of current = 0", "V = IR,Sum of current = 0,Sum of voltage = 0,None"],
    ["FEEE", "Unit 4: Magnetic", "Reluctance kaisa hai?", "Resistance jaisa", "Voltage jaisa,Resistance jaisa,Current jaisa,None"],
    ["FEEE", "Unit 4: Magnetic", "Permeability kiske liye hai?", "Magnetic Material", "Insulator,Magnetic Material,Glass,None"],
    ["FEEE", "Unit 4: Magnetic", "EMF ki unit?", "Volt", "Ampere,Ohm,Volt,Watt"],
    ["FEEE", "Unit 4: Magnetic", "Faraday's Law kisse juda hai?", "Induction", "Gravity,Induction,Friction,None"],
    ["FEEE", "Unit 4: Magnetic", "Power ka formula?", "P = VI", "P = V/I,P = VI,P = I/V,None"],
    ["FEEE", "Unit 4: Magnetic", "Series circuit mein kya same rehta hai?", "Current", "Voltage,Current,Resistance,None"],
    ["FEEE", "Unit 4: Magnetic", "Parallel circuit mein kya same rehta hai?", "Voltage", "Current,Voltage,Power,None"],
    ["FEEE", "Unit 4: Magnetic", "Specific Resistance ki unit?", "Ohm-meter", "Ohm,Ohm-meter,Watt,None"],
    ["FEEE", "Unit 4: Magnetic", "Coulomb kiska unit hai?", "Charge", "Current,Voltage,Charge,None"],
    ["FEEE", "Unit 4: Magnetic", "Lenz's Law kya batata hai?", "Direction of EMF", "Magnitude,Direction of EMF,Speed,None"],
    ["FEEE", "Unit 4: Magnetic", "Hysteresis loss kahan hota hai?", "Core", "Wire,Core,Switch,None"],
    ["FEEE", "Unit 4: Magnetic", "Magnetomotive Force (MMF) unit?", "Ampere-Turns", "Volt,Ampere-Turns,Weber,None"],
    ["FEEE", "Unit 4: Magnetic", "Cork-screw rule kahan use hota hai?", "Magnetic Field", "Voltage,Current,Magnetic Field,None"],
    ["FEEE", "Unit 4: Magnetic", "Work ki unit?", "Joule", "Watt,Joule,Volt,Ampere"],
    ["FEEE", "Unit 4: Magnetic", "Energy Meter kya maapta hai?", "Electrical Energy", "Power,Electrical Energy,Voltage,None"],
    ["FEEE", "Unit 4: Magnetic", "Joule's Law formula?", "H = I^2Rt", "H = IRt,H = VIt,H = I^2Rt,None"],
    ["FEEE", "Unit 5: Machines", "Transformer kis par chalta hai?", "AC", "DC,AC,Both,None"],
    ["FEEE", "Unit 5: Machines", "Step-up transformer kya badhata hai?", "Voltage", "Current,Voltage,Frequency,Power"],
    ["FEEE", "Unit 5: Machines", "Transformer core kiska hota hai?", "Silicon Steel", "Copper,Silicon Steel,Aluminium,None"],
    ["FEEE", "Unit 5: Machines", "DC Motor kis par chalti hai?", "DC", "AC,DC,Both,None"],
    ["FEEE", "Unit 5: Machines", "Induction Motor ka principle?", "RMF", "Static Field,RMF,Self Induction,None"],
    ["FEEE", "Unit 5: Machines", "Synchronous speed formula?", "120f/P", "120P/f,120f/P,60f/P,None"],
    ["FEEE", "Unit 5: Machines", "Transformer mein 'Eddy Current' loss kaise kam karein?", "Lamination", "Copper wire,Lamination,Oil,None"],
    ["FEEE", "Unit 5: Machines", "Alternator kya paida karta hai?", "AC", "DC,AC,Mechanical,None"],
    ["FEEE", "Unit 5: Machines", "Rotor kahan hota hai?", "Ghumne wala part", "Ruka hua part,Ghumne wala part,Bahari part,None"],
    ["FEEE", "Unit 5: Machines", "Stator kaisa part hai?", "Stationary", "Moving,Stationary,Rotating,None"],
    ["FEEE", "Unit 5: Machines", "1-Phase AC voltage India mein?", "230V", "110V,230V,440V,1000V"],
    ["FEEE", "Unit 5: Machines", "Frequency India mein?", "50 Hz", "60 Hz,50 Hz,100 Hz,None"],
    ["FEEE", "Unit 5: Machines", "Motor kya karta hai?", "Elec to Mech", "Mech to Elec,Elec to Mech,Heat to Elec,None"],
    ["FEEE", "Unit 5: Machines", "Generator kya karta hai?", "Mech to Elec", "Elec to Mech,Mech to Elec,Heat to Elec,None"],
    ["FEEE", "Unit 5: Machines", "Slip ka matlab?", "Speed Difference", "Voltage,Speed Difference,Current,None"],
    ["FEEE", "Unit 5: Machines", "DC Generator ka Commutator?", "AC to DC", "DC to AC,AC to DC,Static,None"],
    ["FEEE", "Unit 5: Machines", "Ideal Transformer ki efficiency?", "100%", "50%,80%,90%,100%"],  ["FEEE", "Unit 5: Machines", "Transformer mein 'Oil' ka use?", "Cooling", "Lubrication,Cooling,Heating,None"],
    ["FEEE", "Unit 5: Machines", "Copper loss kahan hota hai?", "Windings", "Core,Windings,Body,None"],
    ["FEEE", "Unit 5: Machines", "Buchholz Relay kahan hoti hai?", "Transformer", "Motor,Generator,Transformer,Switch"],
    ["IT System", "Unit 1: Intro", "Computer ka dimaag kise kehte hain?", "CPU", "RAM,CPU,Monitor,Keyboard"],
    ["IT System", "Unit 1: Intro", "Memory ki sabse chhoti unit kya hai?", "Bit", "Bit,Byte,KB,MB"],
    ["IT System", "Unit 1: Intro", "1 KB mein kitne Bytes hote hain?", "1024", "1000,1024,100,512"],
    ["IT System", "Unit 1: Intro", "RAM ka full form?", "Random Access Memory", "Read Access Memory,Random Access Memory,Ready Memory,None"],
    ["IT System", "Unit 1: Intro", "Inme se kaunsa Output device hai?", "Monitor", "Keyboard,Mouse,Monitor,Scanner"],
    ["IT System", "Unit 1: Intro", "CPU ka mukhya bhag kaunsa hai?", "ALU", "Monitor,ALU,Keyboard,Mouse"],
    ["IT System", "Unit 1: Intro", "ROM kaisa memory hai?", "Non-Volatile", "Volatile,Non-Volatile,Temporary,None"],
    ["IT System", "Unit 1: Intro", "CD ka full form?", "Compact Disc", "Compact Disc,Computer Disc,Central Disc,None"],
    ["IT System", "Unit 1: Intro", "Scanner kaisa device hai?", "Input", "Input,Output,Storage,None"],
    ["IT System", "Unit 1: Intro", "ALU ka full form?", "Arithmetic Logic Unit", "All Logic Unit,Arithmetic Logic Unit,Array Logic Unit,None"],
    ["IT System", "Unit 1: Intro", "Computer ki permanent memory?", "Hard Disk", "RAM,Hard Disk,Cache,None"],
    ["IT System", "Unit 1: Intro", "Mouse kaisa device hai?", "Pointing Device", "Pointing Device,Output Device,Storage,None"],
    ["IT System", "Unit 1: Intro", "1 GB mein kitne MB hote hain?", "1024", "1000,1024,512,2048"],
    ["IT System", "Unit 1: Intro", "Operating System kya hai?", "System Software", "Application Software,System Software,Hardware,None"],
    ["IT System", "Unit 1: Intro", "Modern Computer ke janak?", "Charles Babbage", "Newton,Charles Babbage,Bill Gates,None"],
    ["IT System", "Unit 1: Intro", "UPS ka use kiske liye hota hai?", "Power Backup", "Printing,Power Backup,Scanning,Sound"],
    ["IT System", "Unit 1: Intro", "USB ka full form?", "Universal Serial Bus", "Unique Serial Bus,Universal Serial Bus,Unit Serial Bus,None"],
    ["IT System", "Unit 1: Intro", "Printer ki speed kis mein maapte hain?", "PPM", "KM,PPM,KG,Watts"],
    ["IT System", "Unit 1: Intro", "Motherboard kya hai?", "Circuit Board", "Software,Circuit Board,Monitor,None"],
    ["IT System", "Unit 1: Intro", "SSD ka full form?", "Solid State Drive", "Solid State Drive,Small State Drive,Super Speed Drive,None"],
    ["IT System", "Unit 2: OS", "Windows kisne banaya hai?", "Microsoft", "Apple,Google,Microsoft,IBM"],
    ["IT System", "Unit 2: OS", "Android kiska OS hai?", "Google", "Apple,Google,Microsoft,Nokia"],
    ["IT System", "Unit 2: OS", "Inme se kaunsa OS Open Source hai?", "Linux", "Windows,Mac OS,Linux,None"],
    ["IT System", "Unit 2: OS", "GUI ka matlab?", "Graphical User Interface", "Graphical User Interface,Great User Info,General User Info,None"],
    ["IT System", "Unit 2: OS", "Folder banane ki shortcut key?", "Ctrl+Shift+N", "Ctrl+N,Ctrl+Shift+N,Alt+N,None"],
    ["IT System", "Unit 2: OS", "Taskbar kahan hota hai?", "Bottom of screen", "Top,Bottom of screen,Right,Left"],
    ["IT System", "Unit 2: OS", "Antivirus ka kaam?", "Protect from Virus", "Speed up,Protect from Virus,Cleaning,None"],
    ["IT System", "Unit 2: OS", "Compiler kya hai?", "Language Processor", "Language Processor,Hardware,Output,None"],
    ["IT System", "Unit 2: OS", "Kernel kisika mukhya bhag hai?", "Operating System", "Hardware,Operating System,MS Word,None"],
    ["IT System", "Unit 2: OS", "Safe Mode ka use?", "Troubleshooting", "Gaming,Troubleshooting,Movies,None"],
    ["IT System", "Unit 2: OS", "BIOS kahan store hota hai?", "ROM", "RAM,ROM,Hard Disk,None"],
    ["IT System", "Unit 2: OS", "Device Driver kya hote hain?", "Software", "Hardware,Software,Wires,None"],
    ["IT System", "Unit 2: OS", "Multitasking ka matlab?", "Multiple tasks at once", "One task,Multiple tasks at once,No task,None"],
    ["IT System", "Unit 2: OS", "Virtual Memory kahan hoti hai?", "Hard Disk", "RAM,Hard Disk,CPU,None"],
    ["IT System", "Unit 2: OS", "Trash/Recycle Bin ka kaam?", "Deleted files store karna", "New files,Deleted files store karna,Printing,None"],
    ["IT System", "Unit 3: Office", "MS Word mein Ctrl+S se kya hota hai?", "Save", "Open,Save,Print,New"],
    ["IT System", "Unit 3: Office", "Excel mein Formula shuru hota hai?", "=", "+,=,-,*"],
    ["IT System", "Unit 3: Office", "PowerPoint mein slide show ki key?", "F5", "F1,F5,F10,F12"],
    ["IT System", "Unit 3: Office", "MS Word mein Ctrl+C se kya hota hai?", "Copy", "Cut,Copy,Paste,Undo"],
    ["IT System", "Unit 3: Office", "Excel mein cell ka pata (Address)?", "Column and Row", "Row only,Column and Row,Page number,None"],
    ["IT System", "Unit 3: Office", "Ctrl+V se kya hota hai?", "Paste", "Copy,Paste,Cut,Save"],
    ["IT System", "Unit 3: Office", "Spelling check ki key?", "F7", "F2,F5,F7,F9"],
    ["IT System", "Unit 3: Office", "MS Word mein Landscape kya hai?", "Page Orientation", "Font,Page Orientation,Size,None"],
    ["IT System", "Unit 3: Office", "Excel sheet ka extension?", ".xlsx", ".docx,.xlsx,.pptx,.txt"],
    ["IT System", "Unit 3: Office", "PowerPoint mein nayi slide ki shortcut?", "Ctrl+M", "Ctrl+N,Ctrl+M,Ctrl+S,None"],
    ["IT System", "Unit 3: Office", "Mail Merge kahan hota hai?", "MS Word", "Excel,MS Word,PowerPoint,None"],
    ["IT System", "Unit 3: Office", "Header kahan print hota hai?", "Top of page", "Bottom,Top of page,Middle,None"],
    ["IT System", "Unit 3: Office", "Footer kahan print hota hai?", "Bottom of page", "Top,Bottom of page,Middle,None"],
    ["IT System", "Unit 3: Office", "Find and Replace ki key?", "Ctrl+H", "Ctrl+F,Ctrl+H,Ctrl+G,None"],
    ["IT System", "Unit 3: Office", "Excel mein default sheets?", "1", "1,3,5,10"],
    ["IT System", "Unit 4: Internet", "Internet ka janak?", "Vint Cerf", "Tim Berners-Lee,Vint Cerf,Bill Gates,None"],
    ["IT System", "Unit 4: Internet", "IP ka full form?", "Internet Protocol", "Internet Protocol,Internal Power,Internal Protocol,None"],
    ["IT System", "Unit 4: Internet", "Web Browser ka example?", "Chrome", "Google,Chrome,Windows,None"],
    ["IT System", "Unit 4: Internet", "Search Engine kaunsa hai?", "Google", "Chrome,Google,Firefox,None"],
    ["IT System", "Unit 4: Internet", "HTTP ka full form?", "Hypertext Transfer Protocol", "Hypertext Transfer Protocol,High Transfer,Home Transfer,None"],
    ["IT System", "Unit 4: Internet", "URL ka matlab?", "Uniform Resource Locator", "Uniform Resource Locator,Unique Resource,Universal Resource,None"],
    ["IT System", "Unit 4: Internet", "Email ka matlab?", "Electronic Mail", "Electric Mail,Electronic Mail,Engine Mail,None"],
    ["IT System", "Unit 4: Internet", "LAN ka matlab?", "Local Area Network", "Local Area Network,Long Area,Low Area,None"],
    ["IT System", "Unit 4: Internet", "WAN ka matlab?", "Wide Area Network", "World Area,Wide Area Network,Web Area,None"],
    ["IT System", "Unit 4: Internet", "WiFi ka full form?", "Wireless Fidelity", "Wireless Fidelity,Wireless File,Wireless Find,None"],
    ["IT System", "Unit 4: Internet", "Domain name example?", ".com", ".com,www,http,None"],
    ["IT System", "Unit 4: Internet", "Modem ka kaam?", "Signal conversion", "Printing,Signal conversion,Storage,None"],
    ["IT System", "Unit 4: Internet", "HTML kiske liye use hoti hai?", "Web page design", "Calculation,Web page design,Gaming,None"],
    ["IT System", "Unit 4: Internet", "Cookie kya hai?", "Small text file", "Virus,Small text file,Hardware,None"],
    ["IT System", "Unit 4: Internet", "Social Media example?", "Facebook", "Google,Facebook,Chrome,MS Word"],
    ["IT System", "Unit 5: Security", "Firewall ka kaam?", "Security", "Speed,Security,Design,Storage"],
    ["IT System", "Unit 5: Security", "Strong password example?", "Abc@123", "123456,Password,Abc@123,MyName"],
    ["IT System", "Unit 5: Security", "Phishing kya hai?", "Cyber Crime", "Fishing game,Cyber Crime,Software,None"],
    ["IT System", "Unit 5: Security", "Encryption ka use?", "Data safety", "Data delete,Data safety,Data printing,None"],
    ["IT System", "Unit 5: Security", "Spam mail kya hai?", "Unwanted mail", "Important mail,Unwanted mail,Draft mail,None"],
    ["IT System", "Unit 5: Security", "Hacking ka matlab?", "Unauthorized access", "Authorized access,Unauthorized access,Printing,None"],
    ["IT System", "Unit 5: Security", "VPN ka full form?", "Virtual Private Network", "Virtual Private Network,Very Private,Visual Private,None"],
    ["IT System", "Unit 5: Security", "Two-factor authentication?", "OTP", "Password only,OTP,Fingerprint only,None"],
    ["IT System", "Unit 5: Security", "Cyber Law India mein?", "IT Act 2000", "IT Act 1990,IT Act 2000,IT Act 2010,None"],
    ["IT System", "Unit 5: Security", "Keylogger kya hai?", "Spyware", "Antivirus,Spyware,Hardware,None"],
    ["IT System", "Unit 1: Basic", "RAM kaisi memory hai?", "Temporary", "Permanent,Temporary,Both,None"],
    ["IT System", "Unit 1: Basic", "Binary digits?", "0 and 1", "0 to 9,0 and 1,A and B,None"],
    ["IT System", "Unit 1: Basic", "Input device example?", "Mouse", "Printer,Monitor,Mouse,Speaker"],
    ["IT System", "Unit 1: Basic", "Output device example?", "Printer", "Keyboard,Mouse,Printer,Scanner"],
    ["IT System", "Unit 1: Basic", "1 MB kitne KB ke barabar hai?", "1024", "512,1024,2048,100"],
    ["IT System", "Unit 2: Soft", "Operating system ka udaharan?", "Windows", "MS Word,Windows,Excel,Photoshop"],
    ["IT System", "Unit 2: Soft", "Open source software?", "Android", "Windows,iOS,Android,None"],
    ["IT System", "Unit 2: Soft", "Utility software example?", "Antivirus", "Chrome,Antivirus,Windows,None"],
    ["IT System", "Unit 3: Office", "Presentation software?", "PowerPoint", "Word,Excel,PowerPoint,None"],
    ["IT System", "Unit 3: Office", "Spreadsheet software?", "Excel", "Word,Excel,PowerPoint,None"],
    ["IT System", "Unit 3: Office", "Ctrl+Z se kya hota hai?", "Undo", "Redo,Undo,Save,Copy"],
    ["IT System", "Unit 3: Office", "Ctrl+Y se kya hota hai?", "Redo", "Undo,Redo,Save,Print"],
    ["IT System", "Unit 4: Net", "Network of networks?", "Internet", "LAN,WAN,Internet,None"],
    ["IT System", "Unit 4: Net", "Wireless communication?", "Bluetooth", "Cable,Bluetooth,Fiber,None"],
    ["IT System", "Unit 4: Net", "Browser shortcut for refresh?", "F5", "F1,F2,F5,F10"],
    ["IT System", "Unit 5: Sec", "Computer virus kya hai?", "Program", "Hardware,Program,Animal,None"],
    ["IT System", "Unit 5: Sec", "Digital Signature ka use?", "Authenticity", "Design,Authenticity,Printing,None"],
    ["IT System", "Unit 1: Adv", "SSD fast hai ya HDD?", "SSD", "HDD,SSD,Both same,None"],
    ["IT System", "Unit 1: Adv", "Cache memory kahan hoti hai?", "CPU", "RAM,Hard Disk,CPU,None"],  ["IT System", "Unit 2: Adv", "Dual Boot ka matlab?", "Two OS in one PC", "One OS,Two OS in one PC,No OS,None"],
    ["IT System", "Unit 3: Adv", "Excel mein SUM formula?", "=SUM()", "=ADD(),=SUM(),=TOTAL(),None"],
    ["IT System", "Unit 4: Adv", "FTP ka use?", "File Transfer", "Web browsing,File Transfer,Email,None"],
    ["IT System", "Unit 5: Adv", "Malware ka matlab?", "Malicious Software", "Safe Software,Malicious Software,Free Software,None"],
    ["IT System", "Unit 5: Adv", "Captcha ka use?", "Bot rokne ke liye", "Security,Bot rokne ke liye,Login,None"],
    ["IT System", "Unit 5: Adv", "Cyber bullying kya hai?", "Online harassment", "Offline,Online harassment,Gaming,None"],
["Mathematics-II", "Unit 1", "Determinant of [[1,0],[0,1]]?", "1", "0,1,-1,2"],
["Mathematics-II", "Unit 1", "Cramer's Rule kiske liye hai?", "Linear Equations", "Integration,Linear Equations,Trigonometry,None"],
["Mathematics-II", "Unit 1", "Agar determinant ki do rows same ho?", "0", "1,0,-1,2"],
["Mathematics-II", "Unit 1", "3x3 determinant mein kitne elements hote hain?", "9", "3,6,9,12"],
["Mathematics-II", "Unit 1", "Singular matrix ka determinant kya hota hai?", "0", "1,0,-1,Infinite"],
["Mathematics-II", "Unit 1", "Identity matrix ka determinant?", "1", "0,1,-1,2"],
["Mathematics-II", "Unit 1", "Transpose of a row matrix is?", "Column matrix", "Row matrix,Column matrix,Square matrix,None"],
["Mathematics-II", "Unit 1", "Cramer's rule mein D=0 ho toh?", "No Solution", "Unique Solution,No Solution,One Solution,None"],
["Mathematics-II", "Unit 1", "Minor of an element is a?", "Determinant", "Matrix,Determinant,Vector,None"],
["Mathematics-II", "Unit 1", "Diagonal elements ka sum kya kehlata hai?", "Trace", "Trace,Rank,Determinant,None"],
["Mathematics-II", "Unit 2", "d/dx of sin x?", "cos x", "cos x,-cos x,tan x,sec x"],
["Mathematics-II", "Unit 2", "d/dx of cos x?", "-sin x", "sin x,-sin x,cos x,None"],
["Mathematics-II", "Unit 2", "d/dx of tan x?", "sec^2 x", "sec x,sec^2 x,tan^2 x,None"],
["Mathematics-II", "Unit 2", "d/dx of log x?", "1/x", "x,1/x,e^x,log x"],
["Mathematics-II", "Unit 2", "d/dx of e^x?", "e^x", "e^x,xe^x,1/e^x,0"],
["Mathematics-II", "Unit 2", "d/dx of x^n?", "nx^(n-1)", "x^n,nx^(n-1),n/x,None"],
["Mathematics-II", "Unit 2", "d/dx of constant?", "0", "1,0,constant,None"],
["Mathematics-II", "Unit 2", "d/dx of cot x?", "-cosec^2 x", "sec^2 x,-cosec^2 x,tan x,None"],
["Mathematics-II", "Unit 2", "d/dx of sec x?", "sec x tan x", "tan x,sec x tan x,sec^2 x,None"],
["Mathematics-II", "Unit 2", "d/dx of a^x?", "a^x log a", "a^x,x a^(x-1),a^x log a,None"],
["Mathematics-II", "Unit 2", "Product rule (uv)'?", "u v' + v u'", "uv,u v' - v u',u v' + v u',None"],
["Mathematics-II", "Unit 2", "Quotient rule (u/v)' mein denominator?", "v^2", "v,v^2,u^2,None"],
["Mathematics-II", "Unit 2", "d/dx of sqrt(x)?", "1/(2*sqrt(x))", "1/x,1/(2*sqrt(x)),2*sqrt(x),None"],
["Mathematics-II", "Unit 2", "d/dx of sin^(-1)x?", "1/sqrt(1-x^2)", "1/x,1/sqrt(1-x^2),-1/sqrt(1-x^2),None"],
["Mathematics-II", "Unit 2", "d/dx of tan^(-1)x?", "1/(1+x^2)", "1/x,1/(1+x^2),1/(1-x^2),None"],
["Mathematics-II", "Unit 2", "Function continuous kab hota hai?", "LHL = RHL = f(a)", "LHL = RHL,LHL=f(a),LHL = RHL = f(a),None"],
["Mathematics-II", "Unit 2", "d/dx of 5x^2?", "10x", "5x,10x,x^2,25x"],
["Mathematics-II", "Unit 2", "Second derivative of x^3?", "6x", "3x^2,6x,6,0"],
["Mathematics-II", "Unit 2", "Chain rule kiske liye hai?", "Composite function", "Simple function,Composite function,Constant,None"],
["Mathematics-II", "Unit 2", "d/dx of log(sin x)?", "cot x", "tan x,cot x,1/sin x,None"],
["Mathematics-II", "Unit 3", "Integration of cos x?", "sin x", "sin x,-sin x,tan x,None"],
["Mathematics-II", "Unit 3", "Integration of sin x?", "-cos x", "cos x,-cos x,sin x,None"],
["Mathematics-II", "Unit 3", "Integration of 1/x?", "log x", "x,log x,1/x^2,None"],
["Mathematics-II", "Unit 3", "Integration of e^x?", "e^x", "e^x,log x,x,None"],
["Mathematics-II", "Unit 3", "Integration of x^n?", "x^(n+1)/(n+1)", "nx^(n-1),x^(n+1)/(n+1),x^n,None"],
["Mathematics-II", "Unit 3", "Integration of sec^2 x?", "tan x", "tan x,cot x,sec x,None"],
["Mathematics-II", "Unit 3", "Integration of k dx?", "kx + C", "k,kx + C,x,0"],
["Mathematics-II", "Unit 3", "Definite integral mein 'C' hota hai?", "Nahi", "Haan,Nahi,Kabhi kabhi,None"],
["Mathematics-II", "Unit 3", "Integration of 1/(1+x^2)?", "tan^(-1)x", "sin^(-1)x,tan^(-1)x,log x,None"],
["Mathematics-II", "Unit 3", "Integration of tan x?", "log(sec x)", "sec^2 x,log(sec x),sin x,None"],
["Mathematics-II", "Unit 3", "Integration by parts formula?", "u∫v - ∫(u'∫v)", "uv,u∫v - ∫(u'∫v),u'v',None"],
["Mathematics-II", "Unit 3", "Integration of 0?", "Constant", "0,1,Constant,x"],
["Mathematics-II", "Unit 3", "Area under curve formula?", "∫y dx", "∫x dy,∫y dx,y*x,None"],
["Mathematics-II", "Unit 3", "Integration of cosec^2 x?", "-cot x", "tan x,-cot x,cosec x,None"],
["Mathematics-II", "Unit 3", "Lower limit aur upper limit kis mein hoti hai?", "Definite Integral", "Indefinite,Definite Integral,Derivative,None"],
["Mathematics-II", "Unit 3", "Integration of 1/sqrt(1-x^2)?", "sin^(-1)x", "cos^(-1)x,sin^(-1)x,tan^(-1)x,None"],
["Mathematics-II", "Unit 3", "∫ sin(2x) dx?", "-cos(2x)/2", "cos(2x),-cos(2x)/2,sin(x),None"],
["Mathematics-II", "Unit 3", "∫ e^(2x) dx?", "e^(2x)/2", "e^x,e^(2x)/2,2e^(2x),None"],
["Mathematics-II", "Unit 3", "Integration ka sign kya hai?", "∫", "∂,∑,∫,Δ"],
["Mathematics-II", "Unit 3", "Fundamental Theorem of Calculus kisse juda hai?", "Integration", "Algebra,Integration,Geometry,None"],
["Mathematics-II", "Unit 4", "d2y/dx2 ka order kya hai?", "2", "1,2,3,0"],
["Mathematics-II", "Unit 4", "Degree of (dy/dx)^3 + y = 0?", "3", "1,2,3,None"],
["Mathematics-II", "Unit 4", "Differential Eq mein 'y' kya hai?", "Dependent Variable", "Independent,Dependent Variable,Constant,None"],
["Mathematics-II", "Unit 4", "Linear differential eq ka example?", "dy/dx + Py = Q", "y^2=x,dy/dx + Py = Q,x^2+y^2=1,None"],
["Mathematics-II", "Unit 4", "Integrating Factor (IF) formula?", "e^(∫P dx)", "e^P,e^(∫P dx),∫P dx,None"],
["Mathematics-II", "Unit 4", "Variable separable method kab use hota hai?", "Easy equations", "Matrix,Easy equations,Complex,None"],
["Mathematics-II", "Unit 4", "Order hamesha kaisa hota hai?", "Positive Integer", "Negative,Positive Integer,Fraction,Zero"],
["Mathematics-II", "Unit 4", "Equation jisme derivatives hon?", "Differential Eq", "Quadratic,Differential Eq,Linear,None"],
["Mathematics-II", "Unit 4", "dy/dx = k*y ka solution?", "y = C*e^(kx)", "y=kx,y = C*e^(kx),y=x^2,None"],
["Mathematics-II", "Unit 4", "Degree define hone ke liye eq kaisi honi chahiye?", "Polynomial in derivatives", "Linear,Polynomial in derivatives,Simple,None"],
["Mathematics-II", "Unit 5", "Mean of 10, 20, 30?", "20", "10,20,30,60"],
["Mathematics-II", "Unit 5", "Most frequent value kya kehlati hai?", "Mode", "Mean,Median,Mode,Range"],
["Mathematics-II", "Unit 5", "Median of 1, 2, 3, 4, 5?", "3", "2,3,4,None"],
["Mathematics-II", "Unit 5", "Standard Deviation kiska root hai?", "Variance", "Mean,Variance,Mode,None"],
["Mathematics-II", "Unit 5", "Range ka formula?", "Max - Min", "Max + Min,Max - Min,Mean/2,None"],
["Mathematics-II", "Unit 5", "Sum of observations / Number of observations?", "Mean", "Mean,Median,Mode,None"],
["Mathematics-II", "Unit 5", "Probability ki maximum value?", "1", "0,1,10,100"],
["Mathematics-II", "Unit 5", "Impossible event ki probability?", "0", "0,1,0.5,None"],
["Mathematics-II", "Unit 5", "Variance ki unit?", "Square of unit", "Same,Square of unit,Root,None"],
["Mathematics-II", "Unit 5", "Normal distribution curve kaisa hota hai?", "Bell shaped", "Flat,Bell shaped,Circular,None"],
["Mathematics-II", "Unit 1", "Identity matrix I2?", "[[1,0],[0,1]]", "[[0,1],[1,0]],[[1,0],[0,1]],[[1,1],[1,1]],None"],
["Mathematics-II", "Unit 2", "Derivative of x?", "1", "0,1,x,x^2"],
["Mathematics-II", "Unit 3", "∫ 1 dx?", "x + C", "0,1,x + C,x^2"],
["Mathematics-II", "Unit 5", "Total probability ka sum?", "1", "0,1,0.5,None"],
["Mathematics-II", "Unit 1", "Inverse matrix A^(-1) formula?", "Adj A / |A|", "Adj A,1/|A|,Adj A / |A|,None"],
["Mathematics-II", "Unit 2", "Slope of tangent kya hai?", "dy/dx", "y,x,dy/dx,d2y/dx2"],
["Mathematics-II", "Unit 3", "Integration of cot x?", "log(sin x)", "tan x,log(sin x),sec x,None"],
["Mathematics-II", "Unit 4", "d3y/dx3 ka order?", "3", "1,2,3,None"],
["Mathematics-II", "Unit 5", "Arithmetic Mean formula?", "Σx/n", "Σx,Σx/n,n/Σx,None"],
["Mathematics-II", "Unit 2", "L'Hopital Rule kab lagta hai?", "0/0 form", "1/1 form,0/0 form,Constant,None"],
["Mathematics-II", "Unit 1", "Scalar matrix mein diagonal elements?", "Same", "Different,Same,Zero,None"],
["Mathematics-II", "Unit 2", "d/dx of tan(x)?", "sec^2(x)", "sin,cos,sec^2(x),None"],
["Mathematics-II", "Unit 3", "∫ 1/x dx?", "log|x| + C", "x,log|x| + C,1/x,None"],
["Mathematics-II", "Unit 4", "General solution mein kya hota hai?", "Arbitrary Constants", "Only numbers,Arbitrary Constants,No variables,None"],
["Mathematics-II", "Unit 5", "Coefficient of variation formula?", "(SD/Mean)*100", "SD/Mean,(SD/Mean)*100,Mean/SD,None"],
["Mathematics-II", "Unit 1", "Rank of a matrix kya hai?", "Non-zero rows", "Total rows,Non-zero rows,Zero rows,None"],
["Mathematics-II", "Unit 2", "Velocity kya hai?", "ds/dt", "s*t,ds/dt,d2s/dt2,None"],
["Mathematics-II", "Unit 3", "Area under y=x from 0 to 1?", "0.5", "1,0.5,2,0"],
["Mathematics-II", "Unit 4", "Order of (dy/dx)^2 + d2y/dx2 = 0?", "2", "1,2,4,None"],
["Mathematics-II", "Unit 5", "Standard deviation of a constant?", "0", "1,0,constant,None"],
["Mathematics-II", "Unit 1", "Matrix multiplication possible kab hai?", "Col A = Row B", "Col A = Col B,Col A = Row B,Row A = Col B,None"],
["Mathematics-II", "Unit 2", "d/dx of log(10)?", "0", "1,0,1/10,None"],
["Mathematics-II", "Unit 3", "∫ sec x tan x dx?", "sec x + C", "tan x,sec x + C,sec^2 x,None"],
["Mathematics-II", "Unit 5", "Bar chart kiske liye use hota hai?", "Categorical data", "Calculus,Categorical data,Integration,None"],
["Mathematics-II", "Unit 1", "Square matrix mein Rows aur Columns?", "Equal", "Unequal,Equal,Only 2,None"],
["Mathematics-II", "Unit 2", "Point of maxima par f'(x)?", "0", "1,0,-1,Positive"],
["Mathematics-II", "Unit 3", "∫ dx/(x^2+1)?", "tan^(-1)x + C", "log x,tan^(-1)x + C,sin x,None"],
["Mathematics-II", "Unit 4", "Degree of dy/dx = sin x?", "1", "1,0,Not defined,None"],
["Mathematics-II", "Unit 5", "Sample space of a coin toss?", "{H, T}", "{H},{T},{H, T},None"],
["Mathematics-II", "Unit 2", "d/dx of x^2 + 2x + 1?", "2x + 2", "x+2,2x+2,2x,2"],
["Applied Mechanics", "Unit 1", "Force ki SI unit kya hai?", "Newton", "Pascal,Newton,Joule,Watt"],
["Applied Mechanics", "Unit 1", "Force kaisa quantity hai?", "Vector", "Scalar,Vector,Tensor,None"],
["Applied Mechanics", "Unit 1", "Resultant nikalne ka law?", "Parallelogram Law", "Ohm Law,Parallelogram Law,Boyle Law,None"],
["Applied Mechanics", "Unit 1", "Moment of Force formula?", "Force x Distance", "Force/Distance,Force x Distance,Mass x Acc,None"],
["Applied Mechanics", "Unit 1", "Lami's Theorem kab lagta hai?", "3 Coplanar Forces", "2 Forces,3 Coplanar Forces,4 Forces,None"],
["Applied Mechanics", "Unit 1", "Couple kya paida karta hai?", "Rotation", "Translation,Rotation,Equilibrium,None"],
["Applied Mechanics", "Unit 1", "Equilibrium mein net force?", "Zero", "Zero,Infinite,Positive,Negative"],
["Applied Mechanics", "Unit 1", "Point of application kya hai?", "Jahan force lagta hai", "Center,Jahan force lagta hai,End point,None"],
["Applied Mechanics", "Unit 1", "Rigid body kya hai?", "Jiska shape change na ho", "Solid,Liquid,Jiska shape change na ho,None"],
["Applied Mechanics", "Unit 1", "Transmissibility of force principle kya hai?", "Force can act anywhere on line of action", "Force is fixed,Force can act anywhere on line of action,Force changes,None"],
["Applied Mechanics", "Unit 1", "Coplanar forces ka matlab?", "Ek hi plane mein", "Alag plane mein,Ek hi plane mein,Parallel,None"],
["Applied Mechanics", "Unit 1", "Varignon's Theorem kisse juda hai?", "Moments", "Forces,Moments,Friction,Velocity"],
["Applied Mechanics", "Unit 1", "Clockwise moment kaisa liya jata hai?", "Negative", "Positive,Negative,Zero,None"],
["Applied Mechanics", "Unit 1", "Anticlockwise moment kaisa hota hai?", "Positive", "Positive,Negative,Zero,None"],
["Applied Mechanics", "Unit 1", "Two equal and opposite parallel forces?", "Couple", "Moment,Couple,Resultant,None"],
["Applied Mechanics", "Unit 1", "Force ka effect kis par depend karta hai?", "Magnitude & Direction", "Only Mass,Only Speed,Magnitude & Direction,None"],
["Applied Mechanics", "Unit 1", "Equilibrium ki pehli condition?", "Net Force = 0", "Net Force = 0,Net Moment = 0,Both,None"],
["Applied Mechanics", "Unit 1", "Resultant force kya hai?", "Single force replacing many", "Sum of forces,Single force replacing many,Zero force,None"],
["Applied Mechanics", "Unit 1", "Resolution of force kya hai?", "Splitting a force", "Adding forces,Splitting a force,Zero force,None"],
["Applied Mechanics", "Unit 1", "Polygon Law kiske liye hai?", "More than 2 forces", "Only 2 forces,More than 2 forces,Parallel forces,None"],
["Applied Mechanics", "Unit 1", "Equilibrant force kya hai?", "Force that brings equilibrium", "Resultant,Force that brings equilibrium,Zero,None"],
["Applied Mechanics", "Unit 1", "Concurrent forces kahan milte hain?", "Ek hi point par", "Parallel,Ek hi point par,Kahin nahi,None"],
["Applied Mechanics", "Unit 1", "Non-concurrent forces?", "Jo ek point par na milein", "Jo milte hon,Jo ek point par na milein,Parallel,None"],
["Applied Mechanics", "Unit 1", "Static equilibrium mein body kaisi hoti hai?", "At rest", "Moving,At rest,Rotating,None"],
["Applied Mechanics", "Unit 1", "Scalar quantity ka example?", "Mass", "Force,Mass,Velocity,Acceleration"],
["Applied Mechanics", "Unit 2", "Friction force ki direction?", "Opposite to motion", "Same as motion,Opposite to motion,Perpendicular,None"],
["Applied Mechanics", "Unit 2", "Coefficient of friction (mu)?", "F/N", "N/F,F/N,F*N,None"],
["Applied Mechanics", "Unit 2", "Angle of repose kiske barabar hai?", "Angle of friction", "90 degree,Angle of friction,Zero,None"],
["Applied Mechanics", "Unit 2", "Limiting friction kaisa hota hai?", "Maximum static friction", "Minimum friction,Maximum static friction,Kinetic,None"],
["Applied Mechanics", "Unit 2", "Rolling friction, Sliding se kaisa hota hai?", "Kam", "Zyada,Kam,Barabar,None"],
["Applied Mechanics", "Unit 2", "Lubrication se friction par kya asar padta hai?", "Kam hota hai", "Badhta hai,Kam hota hai,Same rehta hai,None"],
["Applied Mechanics", "Unit 2", "Friction kaisa force hai?", "Self-adjusting", "Constant,Self-adjusting,Active,None"],
["Applied Mechanics", "Unit 2", "Angle of friction ka formula?", "tan theta = mu", "sin theta = mu,tan theta = mu,cos theta = mu,None"],
["Applied Mechanics", "Unit 2", "Cone of friction kahan banta hai?", "At contact point", "At top,At contact point,Inside body,None"],
["Applied Mechanics", "Unit 2", "Dynamic friction Static se kaisa hota hai?", "Kam", "Zyada,Kam,Barabar,None"],
["Applied Mechanics", "Unit 2", "Friction badhane ka tarika?", "Rough surface", "Polishing,Rough surface,Lubrication,None"],
["Applied Mechanics", "Unit 2", "Ball bearings ka use kyun hota hai?", "Friction kam karne", "Friction badhane,Friction kam karne,Weight badhane,None"],
["Applied Mechanics", "Unit 2", "Friction kiske upar depend nahi karta?", "Area of contact", "Material,Area of contact,Roughness,None"],
["Applied Mechanics", "Unit 2", "Co-efficient of friction ki unit?", "No unit", "Newton,Kg,No unit,Pascal"],
["Applied Mechanics", "Unit 2", "Solid friction kaisa hota hai?", "Dry friction", "Fluid friction,Dry friction,Viscosity,None"],
["Applied Mechanics", "Unit 2", "Normal reaction hamesha surface ke?", "Perpendicular", "Parallel,Perpendicular,45 degree,None"],
["Applied Mechanics", "Unit 3", "Rectangle ka CG kahan hota hai?", "Intersection of diagonals", "Corners,Intersection of diagonals,Sides,None"],
["Applied Mechanics", "Unit 3", "Circle ka CG?", "Center point", "Circumference,Center point,Tangent,None"],
["Applied Mechanics", "Unit 3", "Sphere ka CG kahan hota hai?", "Geometric Center", "Surface,Geometric Center,Bottom,None"],
["Applied Mechanics", "Unit 3", "Triangle ka CG (Centroid)?", "h/3 from base", "h/2,h/3 from base,h/4,None"],
["Applied Mechanics", "Unit 3", "Centroid kiske liye use hota hai?", "Plane areas", "Solid bodies,Plane areas,Liquids,None"],
["Applied Mechanics", "Unit 3", "Cylinder ka CG kahan hota hai?", "Mid-point of axis", "Base,Top,Mid-point of axis,None"],
["Applied Mechanics", "Unit 3", "Cone ka CG from base?", "h/4", "h/2,h/3,h/4,h/5"],
["Applied Mechanics", "Unit 3", "Hemisphere ka CG from base?", "3r/8", "r/2,3r/8,4r/3,None"],
["Applied Mechanics", "Unit 3", "Centroid aur CG same kab hote hain?", "Uniform density mein", "Hamesha,Uniform density mein,Kabhi nahi,None"],
["Applied Mechanics", "Unit 3", "T-section ka CG kis axis par hota hai?", "Axis of symmetry", "X-axis,Y-axis,Axis of symmetry,None"],
["Applied Mechanics", "Unit 3", "Semicircle ka CG from base?", "4r/3pi", "r/2,4r/3pi,2r/pi,None"],
["Applied Mechanics", "Unit 3", "Thin rod ka CG kahan hota hai?", "Middle of rod", "Ends,Middle of rod,One-third,None"],
["Applied Mechanics", "Unit 3", "Circle ki symmetry?", "About every diameter", "Only X-axis,Only Y-axis,About every diameter,None"],
["Applied Mechanics", "Unit 3", "Hollow cone ka CG from base?", "h/3", "h/2,h/3,h/4,None"],
["Applied Mechanics", "Unit 4", "Mechanical Advantage (MA)?", "W/P", "P/W,W/P,V1/V2,None"],
["Applied Mechanics", "Unit 4", "Velocity Ratio (VR)?", "Distance by Effort/Load", "W/P,Distance by Effort/Load,P/W,None"],
["Applied Mechanics", "Unit 4", "Efficiency ka formula?", "MA/VR", "MA*VR,MA/VR,VR/MA,None"],
["Applied Mechanics", "Unit 4", "Ideal machine ki efficiency?", "100%", "50%,90%,100%,120%"],
["Applied Mechanics", "Unit 4", "Reversible machine ki efficiency?", "> 50%", "< 50%,> 50%,100%,None"],
["Applied Mechanics", "Unit 4", "Simple wheel and axle kaisa device hai?", "Lifting machine", "Cutting machine,Lifting machine,Measuring,None"],
["Applied Mechanics", "Unit 4", "Screw Jack ka use?", "Bhaari load uthane", "Cutting,Bhaari load uthane,Fastening,None"],
["Applied Mechanics", "Unit 4", "Law of machine?", "P = mW + C", "P = W,P = mW + C,MA = VR,None"],
["Applied Mechanics", "Unit 4", "Effort lost in friction?", "P - W/VR", "P + W/VR,P - W/VR,W - P,None"],
["Applied Mechanics", "Unit 4", "Machine jisme friction zero ho?", "Ideal Machine", "Simple Machine,Ideal Machine,Complex Machine,None"],
["Applied Mechanics", "Unit 4", "Load (W) aur Effort (P) ka ratio?", "Mechanical Advantage", "Velocity Ratio,Mechanical Advantage,Efficiency,None"],
["Applied Mechanics", "Unit 4", "Velocity ratio of 1st system of pulleys?", "2^n", "n,2^n,2n,None"],
["Applied Mechanics", "Unit 4", "Velocity ratio of 2nd system of pulleys?", "n", "n,2n,n^2,None"],
["Applied Mechanics", "Unit 4", "Differential wheel and axle ka VR?", "2D/(d1-d2)", "D/d,2D/(d1-d2),W/P,None"],
["Applied Mechanics", "Unit 4", "Worm and worm wheel ka VR?", "RT/r", "R/r,RT/r,T/2,None"],
["Applied Mechanics", "Unit 4", "Non-reversible machine ko kya kehte hain?", "Self-locking machine", "Ideal machine,Self-locking machine,Reversible,None"],
["Applied Mechanics", "Unit 4", "Self-locking machine ki efficiency?", "Less than 50%", "More than 50%,Less than 50%,100%,None"],
["Applied Mechanics", "Unit 4", "Screw jack ka lead kya hai?", "Pitch (p)", "Diameter,Pitch (p),Radius,None"],
["Applied Mechanics", "Unit 4", "MA hamesha VR se kaisa hota hai?", "Kam (Practical mein)", "Zyada,Kam (Practical mein),Barabar,None"],
["Applied Mechanics", "Unit 4", "Friction in machine formula?", "P - Pi", "W - P,P - Pi,MA/VR,None"],
["Applied Mechanics", "Unit 4", "Velocity ratio constant rehta hai?", "Haan", "Haan,Nahi,Sirf ideal mein,None"],
["Applied Mechanics", "Unit 4", "Geared pulley block ka VR?", "D/d * T1/T2", "W/P,D/d * T1/T2,n,None"],
["Applied Mechanics", "Unit 4", "Input of machine formula?", "Effort x Distance of effort", "Load x Distance,Effort x Distance of effort,MA/VR,None"],
["Applied Mechanics", "Unit 4", "Output of machine formula?", "Load x Distance of load", "P x d,Load x Distance of load,Efficiency,None"],
["Applied Mechanics", "Unit 4", "Ideal effort (Pi) formula?", "W/VR", "W*VR,W/VR,P/MA,None"],
["Applied Mechanics", "Unit 5", "Newton's 2nd Law equation?", "F = ma", "v = u + at,F = ma,P = mv,None"],
["Applied Mechanics", "Unit 5", "Work done formula?", "F x d", "F/d,F x d,m x g,None"],
["Applied Mechanics", "Unit 5", "Kinetic Energy formula?", "1/2 mv^2", "mgh,1/2 mv^2,mv,None"],
["Applied Mechanics", "Unit 5", "Potential Energy formula?", "mgh", "mgh,1/2 mv^2,ma,None"],
["Applied Mechanics", "Unit 5", "Power ki unit?", "Watt", "Joule,Watt,Newton,None"],
["Applied Mechanics", "Unit 5", "Momentum ka formula?", "p = mv", "p = m/v,p = mv,p = ma,None"],
["Applied Mechanics", "Unit 5", "1 Watt kiske barabar hai?", "1 Joule/sec", "1 Newton/sec,1 Joule/sec,1 kg/sec,None"],
["Applied Mechanics", "Unit 5", "Impulse ka formula?", "Force x Time", "Mass x Vel,Force x Time,Work/Time,None"],
["Applied Mechanics", "Unit 5", "Newton's 1st Law ka doosra naam?", "Law of Inertia", "Law of Gravity,Law of Inertia,Law of Force,None"],
["Applied Mechanics", "Unit 5", "Rate of change of momentum?", "Force", "Work,Force,Power,Energy"],
["Applied Mechanics", "Unit 5", "Work-Energy principle kya hai?", "Work = Change in KE", "Work = Force,Work = Change in KE,Work = PE,None"],
["Applied Mechanics", "Unit 5", "Power ki practical unit?", "Horse Power (HP)", "Watt,Joule,Horse Power (HP),None"],
["Applied Mechanics", "Unit 5", "1 HP in Watts?", "746 W", "700 W,746 W,1000 W,None"],
["Applied Mechanics", "Unit 5", "Energy kaisa quantity hai?", "Scalar", "Vector,Scalar,Tensor,None"],
["Applied Mechanics", "Unit 5", "Joule kiska unit hai?", "Work and Energy", "Force,Power,Work and Energy,None"],
["Applied Mechanics", "Unit 5", "Acceleration ki SI unit?", "m/s^2", "m/s,m/s^2,km/h,None"],
["Applied Mechanics", "Unit 5", "Torque ka formula?", "Force x Radius", "Mass x Acc,Force x Radius,Work/Time,None"],
["Applied Mechanics", "Unit 5", "Centripetal force direction?", "Towards center", "Away from center,Towards center,Parallel,None"],
["Applied Mechanics", "Unit 5", "1 Joule kiske barabar hai?", "1 N-m", "1 N/m,1 N-m,1 Watt,None"],
["Applied Mechanics", "Unit 5", "Momentum conservation?", "Initial P = Final P", "Force = 0,Initial P = Final P,Mass = 0,None"],
["Environmental", "Unit 1: Ecology", "Ecosystem ka mukhya source kya hai?", "Sun", "Water,Air,Sun,Soil"],
["Environmental", "Unit 1: Ecology", "Biotic component ka example?", "Plants", "Air,Water,Plants,Soil"],
["Environmental", "Unit 1: Ecology", "Abiotic component kaunsa hai?", "Temperature", "Animals,Plants,Temperature,Bacteria"],
["Environmental", "Unit 1: Ecology", "Food Chain mein producers kaun hote hain?", "Green Plants", "Animals,Green Plants,Fungi,None"],
["Environmental", "Unit 1: Ecology", "Ecology shabd kisne diya?", "Ernst Haeckel", "Darwin,Newton,Ernst Haeckel,None"],
["Environmental", "Unit 1: Ecology", "Biodiversity ka matlab?", "Vividh prakar ke jeev", "Sirf plants,Vividh prakar ke jeev,Sirf animals,None"],
["Environmental", "Unit 2: Pollution", "Air pollution ka mukhya karan?", "Fossil Fuel Burning", "Wind,Fossil Fuel Burning,Rain,Trees"],
["Environmental", "Unit 2: Pollution", "Acid Rain kiske karan hoti hai?", "SO2 and NO2", "CO2,SO2 and NO2,Oxygen,Nitrogen"],
["Environmental", "Unit 2: Pollution", "Water pollution se kaunsi bimari hoti hai?", "Cholera", "Malaria,Cholera,Asthma,None"],
["Environmental", "Unit 2: Pollution", "Noise pollution ki unit?", "Decibel", "Watt,Decibel,Hertz,Joule"],
["Environmental", "Unit 2: Pollution", "Global Warming ke liye mukhya gas?", "CO2", "Oxygen,CO2,Nitrogen,Helium"],
["Environmental", "Unit 2: Pollution", "Ozone layer kahan payi jati hai?", "Stratosphere", "Troposphere,Stratosphere,Mesosphere,None"],
["Environmental", "Unit 2: Pollution", "Ozone hole ka karan?", "CFC", "CO2,CFC,CH4,None"],
["Environmental", "Unit 3: Energy", "Renewable energy source kaunsa hai?", "Solar Energy", "Coal,Petrol,Solar Energy,Nuclear"],
["Environmental", "Unit 3: Energy", "Non-renewable energy source?", "Coal", "Wind,Solar,Coal,Biomass"],
["Environmental", "Unit 3: Energy", "CNG ka full form?", "Compressed Natural Gas", "Common Natural Gas,Compressed Natural Gas,Cool Gas,None"],
["Environmental", "Unit 3: Energy", "LPG mein mukhya gas kaunsi hoti hai?", "Butane", "Methane,Butane,Oxygen,None"],
["Environmental", "Unit 4: Issues", "Greenhouse effect se kya hota hai?", "Earth ka temp badhta hai", "Thand badhti hai,Earth ka temp badhta hai,Barish hoti hai,None"],
["Environmental", "Unit 4: Issues", "Deforestation ka matlab?", "Pedon ki katai", "Ped lagana,Pedon ki katai,Kheti karna,None"],
["Environmental", "Unit 4: Issues", "World Environment Day kab manaya jata hai?", "5th June", "1st May,5th June,15th August,None"],
["Environmental", "Unit 4: Issues", "Sustainable Development kya hai?", "Bhavishya ke liye bachat", "Zyada kharch,Bhavishya ke liye bachat,Sirf aaj ka sochna,None"],
["Environmental", "Unit 4: Issues", "Chipko Movement kisse juda tha?", "Forest Protection", "Water,Forest Protection,Air,None"],
["Environmental", "Unit 5: Acts", "Air Act kab pass hua?", "1981", "1974,1981,1986,2000"],
["Environmental", "Unit 5: Acts", "Water Act kab pass hua?", "1974", "1974,1981,1986,None"],
["Environmental", "Unit 5: Acts", "EPA (Env Protection Act) kab aaya?", "1986", "1980,1986,1992,None"],
["Environmental", "Unit 1", "Photosynthesis mein kaunsi gas nikalti hai?", "Oxygen", "CO2,Oxygen,Nitrogen,None"],
["Environmental", "Unit 2", "Smog kiska mixture hai?", "Smoke and Fog", "Smoke and Air,Smoke and Fog,Fog and Dust,None"],
["Environmental", "Unit 3", "Biogas ka mukhya component?", "Methane", "Butane,Methane,Propane,None"],
["Environmental", "Unit 4", "Rain water harvesting ka fayda?", "Ground water badhta hai", "Flood aata hai,Ground water badhta hai,Paani ganda hota hai,None"],
["Environmental", "Unit 1", "Herbivores kya khate hain?", "Plants", "Meat,Plants,Both,None"],
["Environmental", "Unit 2", "Minamata disease kiske karan hui?", "Mercury", "Lead,Mercury,Cadmium,None"],
["Environmental", "Unit 2", "Bhopal Gas Tragedy mein kaunsi gas thi?", "MIC", "CO,MIC,CFC,None"],
["Environmental", "Unit 3", "Geothermal energy kahan se milti hai?", "Earth's Heat", "Sun,Wind,Earth's Heat,None"],
["Environmental", "Unit 4", "Solid Waste Management mein 3R kya hai?", "Reduce, Reuse, Recycle", "Red, Run, Race,Reduce, Reuse, Recycle,Remove,None"],
["Environmental", "Unit 1", "Omnivores ka example?", "Human", "Lion,Cow,Human,Deer"],
["Environmental", "Unit 2", "DDT kya hai?", "Pesticide", "Fertilizer,Pesticide,Medicine,None"],
["Environmental", "Unit 3", "Nuclear energy ka raw material?", "Uranium", "Coal,Uranium,Iron,None"],
["Environmental", "Unit 5", "Wild Life Protection Act?", "1972", "1972,1980,1990,None"],
["Environmental", "Unit 1", "Decomposers kaun hote hain?", "Bacteria & Fungi", "Plants,Animals,Bacteria & Fungi,None"],
["Environmental", "Unit 2", "E-waste ka matlab?", "Electronic waste", "Easy waste,Electronic waste,Earth waste,None"],
["Environmental", "Unit 1", "Ecosystem ka sabse bada part?", "Biosphere", "Community,Biosphere,Population,None"],
["Environmental", "Unit 2", "Lead pollution se kya kharab hota hai?", "Brain", "Legs,Brain,Hair,None"],
["Environmental", "Unit 3", "Wind mill kya banati hai?", "Electricity", "Water,Electricity,Heat,None"],
["Environmental", "Unit 4", "Earth Day kab hota hai?", "22nd April", "22nd April,1st Jan,5th June,None"],
["Environmental", "Unit 1", "Energy flow kaisa hota hai?", "Unidirectional", "Cyclic,Unidirectional,Both,None"],
["Environmental", "Unit 2", "Primary pollutant kaunsa hai?", "CO", "Ozone,CO,PAN,None"],
["Environmental", "Unit 2", "Secondary pollutant kaunsa hai?", "Ozone", "CO,CO2,Ozone,None"],
["Environmental", "Unit 3", "Tidal energy kahan se aati hai?", "Tides", "Rivers,Tides,Rain,None"],
["Environmental", "Unit 4", "Kyoto Protocol kiske liye tha?", "Climate Change", "Water,Climate Change,Forest,None"],
["Environmental", "Unit 1", "Pyramid of Energy hamesha kaisa hota hai?", "Upright", "Inverted,Upright,Horizontal,None"],
["Environmental", "Unit 2", "Particulate matter (PM) kahan hota hai?", "Air", "Water,Air,Soil,None"],
["Environmental", "Unit 3", "Hydro-power kisse banti hai?", "Water", "Air,Water,Sun,None"],
["Environmental", "Unit 4", "Red Data Book kiske liye hai?", "Endangered species", "Plants,Endangered species,All animals,None"],
["Environmental", "Unit 5", "Forest Conservation Act kab aaya?", "1980", "1970,1980,1990,None"],
["Environmental", "Unit 1", "Niche ka matlab?", "Role of organism", "Home,Role of organism,Food,None"],
["Environmental", "Unit 2", "Biological Oxygen Demand (BOD) kya maapta hai?", "Water Pollution", "Air Pollution,Water Pollution,Soil,None"],
["Environmental", "Unit 3", "Fossil fuels ko banne mein kitna samay lagta hai?", "Millions of years", "10 years,100 years,Millions of years,None"],
["Environmental", "Unit 4", "Coral reefs ko khatra kisse hai?", "Global Warming", "Rain,Global Warming,Wind,None"],
["Environmental", "Unit 1", "Food web kya hai?", "Network of food chains", "Single chain,Network of food chains,None,None"],
["Environmental", "Unit 2", "Thermal pollution kahan se aata hai?", "Power Plants", "Cars,Power Plants,Farms,None"],
["Environmental", "Unit 3", "Solar cell kiska bana hota hai?", "Silicon", "Copper,Silicon,Iron,None"],
["Environmental", "Unit 4", "Soil Erosion kaise rokein?", "Afforestation", "Cutting trees,Afforestation,Overgrazing,None"],
["Environmental", "Unit 1", "10% Law energy transfer kisne diya?", "Lindeman", "Darwin,Lindeman,Haeckel,None"],
["Environmental", "Unit 2", "Fly ash kahan se nikalti hai?", "Thermal Power Plant", "Cars,Thermal Power Plant,Mines,None"],
["Environmental", "Unit 3", "India mein sabse zyada energy source?", "Coal", "Solar,Coal,Wind,None"],
["Environmental", "Unit 4", "Endemic species kya hain?", "Jo sirf ek jagah milein", "Sab jagah,Jo sirf ek jagah milein,Jo mar gayi hon,None"],
["Environmental", "Unit 1", "Aquatic ecosystem ka example?", "Pond", "Forest,Pond,Desert,None"],
["Environmental", "Unit 2", "Noise level residential area mein (Day)?", "55 dB", "55 dB,75 dB,90 dB,None"],
["Environmental", "Unit 3", "Photovoltaic effect kisse juda hai?", "Solar Energy", "Wind,Solar Energy,Nuclear,None"],
["Environmental", "Unit 4", "Desertification ka karan?", "Overgrazing", "Rain,Overgrazing,Afforestation,None"],
["Environmental", "Unit 1", "Symbiosis ka example?", "Lichen", "Bacteria,Lichen,Grass,None"],
["Environmental", "Unit 2", "Landfill se kaunsi gas nikalti hai?", "Methane", "Oxygen,Methane,Nitrogen,None"],
["Environmental", "Unit 3", "Uranium-235 kya hai?", "Nuclear Fuel", "Coal,Nuclear Fuel,Metal,None"],
["Environmental", "Unit 4", "In-situ conservation ka example?", "National Park", "Zoo,National Park,Botanic Garden,None"],
["Environmental", "Unit 5", "CPCB ka full form?", "Central Pollution Control Board", "Central Power,Central Pollution Control Board,Common Board,None"],
["Environmental", "Unit 1", "Parasite ka example?", "Cuscuta", "Mango,Cuscuta,Rose,None"],
["Environmental", "Unit 2", "Oil spill kahan hota hai?", "Oceans", "Land,Rivers,Oceans,None"],
["Environmental", "Unit 3", "Ocean Thermal Energy (OTEC) kya hai?", "Temp difference energy", "Wave energy,Temp difference energy,Wind,None"],
["Environmental", "Unit 4", "Ex-situ conservation ka example?", "Zoo", "National Park,Zoo,Wild Life Sanctuary,None"],
["Environmental", "Unit 1", "Lotic water kaisa hota hai?", "Behta hua", "Ruka hua,Behta hua,Ganda,None"],
["Environmental", "Unit 2", "Hardness of water kiski wajah se?", "Calcium & Magnesium", "Sodium,Calcium & Magnesium,Iron,None"],
["Environmental", "Unit 3", "Anemometer kya maapta hai?", "Wind Speed", "Solar,Wind Speed,Pressure,None"],
["Environmental", "Unit 4", "Hotspots kiske liye hain?", "Biodiversity", "Heat,Biodiversity,Volcano,None"],
["Environmental", "Unit 1", "Lentic water kaisa hota hai?", "Ruka hua (Pond)", "Behta hua,Ruka hua (Pond),Sea,None"],
["Environmental", "Unit 2", "Green muffler kiske liye use hota hai?", "Noise Pollution", "Air Pollution,Noise Pollution,Water,None"],
["Environmental", "Unit 3", "Solar cooker mein kaunsa mirror?", "Concave", "Convex,Concave,Plain,None"],
["Environmental", "Unit 4", "Montreal Protocol kiske liye tha?", "Ozone Protection", "Water,Ozone Protection,Soil,None"],
["Environmental", "Unit 1", "Trophic level 1 par kaun hota hai?", "Producers", "Herbivores,Producers,Carnivores,None"],
["Environmental", "Unit 2", "Pyrolysis kiske liye hai?", "Waste to Energy", "Cleaning,Waste to Energy,Watering,None"],
["Environmental", "Unit 3", "Active solar system mein kya hota hai?", "Pump/Fan use hote hain", "Direct sun,Pump/Fan use hote hain,None,None"],
["Environmental", "Unit 4", "Salinization kahan hota hai?", "Soil", "Air,Water,Soil,None"],
["Environmental", "Unit 1", "Saprotrophs kya khate hain?", "Dead matter", "Plants,Dead matter,Insects,None"],
["Environmental", "Unit 2", "Incineration kya hai?", "Burning waste", "Burying waste,Burning waste,Recycling,None"],
["Environmental", "Unit 3", "Bio-diesel kisse banta hai?", "Jatropha", "Coal,Jatropha,Petrol,None"],
["Environmental", "Unit 4", "Siltation kahan hota hai?", "Dams/Rivers", "Air,Dams/Rivers,Forest,None"],
["Environmental", "Unit 5", "NGT ka full form?", "National Green Tribunal", "National Gas,National Green Tribunal,New Green Team,None"],
["Environmental", "Unit 1", "Biomagnification kya hai?", "Toxic badhna", "Energy badhna,Toxic badhna,Size badhna,None"],
["Environmental", "Unit 2", "Aerosols kahan paye jate hain?", "Air", "Water,Air,Food,None"],
["Environmental", "Unit 3", "Pellets kisse bante hain?", "Biomass", "Coal,Biomass,Iron,None"],
["Environmental", "Unit 4", "Green data book kiske liye hai?", "Environmental data", "Endangered species,Environmental data,Animals,None"]
    ]
# Session states initialize
if 'score' not in st.session_state: st.session_state.score = 0
if 'current_q' not in st.session_state: st.session_state.current_q = 0
if 'quiz_started' not in st.session_state: st.session_state.quiz_started = False
if 'quiz_data' not in st.session_state: st.session_state.quiz_data = []

# --- BRANDING ---
st.title("🎓 Polytechnic Exam Quiz 2026")
st.caption("Created by: Jigar Dubey")
if not st.session_state.quiz_started:
        # 1. User Name Input
        user_name = st.text_input("👤 Apna Poora Naam Likhein:", key="user_name_input")
        
        # 2. Subject Selection
        subs = sorted(list(set([x[0] for x in st.session_state.db])))
        selected_sub = st.selectbox("📚 Apna Subject Chuniye:", subs)
        
        # 3. Unit Selection
        units = sorted(list(set([x[1] for x in st.session_state.db if x[0] == selected_sub])))
        selected_unit = st.selectbox("📖 Ab Unit (Chapter) Chuniye:", units)
        
            if st.button("🚀 Start Quiz"):
        if user_name.strip() == "":
            st.error("Bhai, bina naam ke entry nahi milegi!")
        else:
            # Setup session for the quiz
            st.session_state.user_name = user_name
            st.session_state.quiz_data = [
                x for x in st.session_state.db 
                if x[0] == selected_sub and x[1] == selected_unit
            ]
            random.shuffle(st.session_state.quiz_data)
            st.session_state.score = 0
            st.session_state.current_q = 0
            st.session_state.quiz_started = True
            if 'score_saved' in st.session_state: del st.session_state.score_saved
            st.rerun()

else:
    # --- Quiz Logic (Running Mode) ---
    q_list = st.session_state.quiz_data
    if st.session_state.current_q < len(q_list):
        curr = q_list[st.session_state.current_q]

        # Sawal number aur progress bar
        st.write(f"***Sawal {st.session_state.current_q + 1} of {len(q_list)}***")
        st.progress((st.session_state.current_q + 1) / len(q_list))
        st.info(curr[2]) # Sawal dikhana

        # Options logic
        options_raw = curr[4].split(',')
        options = [opt.strip() for opt in options_raw if opt.strip()]
        user_ans = st.radio("Sahi option chuniye:", options, key=f"q_{st.session_state.current_q}")

        # --- SIMPLE TIMER ---
        if 'start_time' not in st.session_state:
            st.session_state.start_time = time.time()

        limit = 30
        elapsed = time.time() - st.session_state.start_time
        remaining = max(0, int(limit - elapsed))

        if remaining > 0:
            st.write(f"⏱️ **Time Left: {remaining}s**")
        else:
            st.error("⏰ Time's Up!")
            if 'start_time' in st.session_state: del st.session_state.start_time
            st.session_state.current_q += 1
            st.rerun()

        if st.button("Submit Answer"):
            if user_ans.strip() == curr[3].strip():
                st.success("✅ **Sahi Jawab!**")
                st.balloons()
                st.session_state.score += 1
            else:
                st.error("❌ **Galat Jawab!**")
                st.info(f"💡 Sahi uttar tha: **{curr[3]}**")

            time.sleep(2)
            if 'start_time' in st.session_state: del st.session_state.start_time
            st.session_state.current_q += 1
            st.rerun()

        # Result Screen
        st.balloons()
        st.header(f"🏁 Quiz Result: {st.session_state.score}/{len(q_list)}")
        
        # Performance message based on score
        if st.session_state.score == len(q_list):
            st.success("Kya baat hai! Tum toh genius ho! 🏆")
        elif st.session_state.score > len(q_list) / 2:
            st.info("Bohot badhiya! Thodi aur mehnat karo. 💪")
        else:
            st.warning("Koi baat nahi, dobara koshish karo! 📚")
        # --- LEADERBOARD ---
        st.divider()
        st.subheader("🏆 Leaderboard")
       
            if name:
                # CSV file mein score save karna
                with open("scores.csv", "a") as f:
                    f.write(f"{name},{st.session_state.score},{len(q_list)}\n")
                st.success("Score save ho gaya! Page refresh karke check karein.")
            else:
                st.error("Pehle naam toh likho bhai!")

        # Leaderboard Table dikhana
        try:
                        # Purana data load karo
            data = pd.read_csv("scores.csv", names=["Naam", "Score", "Total"])
            
            # --- AGGREGATION LOGIC (Sab jod do) ---
            # Har bande ke naam ke hisab se Score aur Total ko plus (+) karega
            leaderboard = data.groupby("Naam").sum().reset_index()
            
            # Highest total marks wale ko top par dikhao
            leaderboard = leaderboard.sort_values(by="Score", ascending=False).head(10)
            
            # Rank dikhane ke liye (1, 2, 3...)
            leaderboard.index = leaderboard.index + 1
            st.table(leaderboard)
            
            st.table(data)
        except:
            st.info("Abhi tak koi topper nahi hai. Pehle bano!")
            
        if st.button("Main Menu par wapas jayein"):
            st.session_state.quiz_started = False
            st.session_state.quiz_data = []
            st.rerun()
