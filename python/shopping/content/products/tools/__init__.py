def analyze_variants(variants):
    colors = {}
    
    # Size abbreviation mapping
    size_mapping = {
        'S': 'Small',
        'M': 'Medium',
        'L': 'Large',
        'XL': 'ExtraLarge'
    }
    
    # Loop through each variant
    for variant in variants:
        # Extract the first item (color-size info)
        color_size = variant[0]
        
        # Split the color and size
        color, size = color_size.split('-')
        
        # If size is a known abbreviation, map it to full name
        if size in size_mapping:
            size = size_mapping[size]
        else:
            # For sizes like XXL, XXXL, etc., replace the last "L" with "Large"
            if size.endswith('L'):
                size = size[:-1] + 'Large'
        
        # Initialize color in dictionary if not already present
        if color not in colors:
            colors[color] = []
        
        # Append the size to the corresponding color key
        colors[color].append(size)
    
    # Add a 'total' key with the count of color keys
    colors_total = len(colors)
    
    return [colors, colors_total]


