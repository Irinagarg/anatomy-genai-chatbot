 def anatomy_response(user_input):
    user_input = user_input.lower()

    if "heart" in user_input:
        return """
         HEART:


     

        The heart is a hollow, muscular organ responsible for pumping blood 
        throughout the circulatory system. It maintains continuous blood flow 
        to deliver oxygen and nutrients to tissues and remove carbon dioxide.

        Location:
        - Middle mediastinum of the thoracic cavity
        - Slightly tilted toward the left side

         Structure:
        - Four chambers:
            • Right Atrium
            • Right Ventricle
            • Left Atrium
            • Left Ventricle
        - Septum separates right and left sides
        - Valves:
            • Tricuspid valve
            • Pulmonary valve
            • Mitral (Bicuspid) valve
            • Aortic valve

        Circulation:
        - Pulmonary circulation → Heart ↔ Lungs
        - Systemic circulation → Heart ↔ Body

        Electrical System:
        - SA node (natural pacemaker)
        - AV node
        - Bundle of His & Purkinje fibers

        Major Blood Vessels:
        - Aorta
        - Pulmonary arteries
        - Pulmonary veins
        - Superior & Inferior vena cava
        """

    elif "brain" in user_input:
        return """
         BRAIN:

        The brain is the central control organ of the nervous system. 
        It regulates voluntary and involuntary functions and enables cognition.

         Location:
        - Cranial cavity
        - Protected by skull, meninges, and cerebrospinal fluid

         Major Parts:
        1. Cerebrum:
            • Largest part
            • Controls thinking, memory, speech, voluntary movement
            • Divided into frontal, parietal, temporal, occipital lobes

        2. Cerebellum:
            • Coordinates balance and fine motor control

        3. Brainstem:
            • Midbrain, Pons, Medulla oblongata
            • Controls breathing, heart rate, reflexes

         Functional Areas:
        - Motor cortex
        - Sensory cortex
        - Broca’s area (speech)
        - Wernicke’s area (language comprehension)

         Protection:
        - Meninges (Dura mater, Arachnoid mater, Pia mater)
        - Cerebrospinal fluid cushioning
        """

    elif "lungs" in user_input:
        return """
         LUNGS:

        The lungs are paired respiratory organs responsible for gas exchange 
        between the body and the external environment.

         Location:
        - Thoracic cavity
        - Protected by rib cage
        - Right lung has 3 lobes
        - Left lung has 2 lobes

         Airway Structure:
        - Trachea
        - Bronchi
        - Bronchioles
        - Alveoli (site of gas exchange)

         Gas Exchange:
        - Oxygen diffuses into blood
        - Carbon dioxide diffuses out
        - Occurs in alveolar-capillary membrane

         Function:
        - Supplies oxygen to bloodstream
        - Removes carbon dioxide waste
        - Maintains blood pH balance

         Surfactant:
        - Reduces surface tension
        - Prevents alveolar collapse
        """

    elif "liver" in user_input:
        return """
         LIVER:

        The liver is the largest internal organ and a major metabolic center.

         Location:
        - Upper right quadrant of abdomen
        - Below diaphragm

         Structure:
        - Divided into right and left lobes
        - Made of hepatic lobules
        - Functional unit: Hepatocyte

         Functions:
        - Detoxification of toxins and drugs
        - Metabolism of carbohydrates, fats, proteins
        - Storage of glycogen
        - Production of bile
        - Synthesis of clotting factors
        - Breakdown of hemoglobin

        Blood Supply:
        - Hepatic artery (oxygenated blood)
        - Portal vein (nutrient-rich blood)

        🧪 Additional Role:
        - Immune function via Kupffer cells
        """

    elif "kidney" in user_input or "kidneys" in user_input:
        return """
         KIDNEYS:

        The kidneys are bean-shaped organs responsible for filtration 
        and maintenance of homeostasis.

         Location:
        - Retroperitoneal space
        - On either side of vertebral column

         Structure:
        - Renal cortex
        - Renal medulla
        - Renal pelvis

         Functional Unit:
        - Nephron
            • Glomerulus (filtration)
            • Bowman’s capsule
            • Loop of Henle
            • Collecting duct

         Functions:
        - Removes nitrogenous wastes
        - Regulates electrolyte balance
        - Controls blood pressure (Renin)
        - Produces erythropoietin (RBC production)
        - Maintains acid-base balance

         Forms urine for excretion
        """

    else:
        return "Please ask about Heart, Brain, Lungs, Liver, or Kidneys."
