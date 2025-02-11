def analyze_variants(variants):
    colors = {}
    
    # Size abbreviation mapping
    size_mapping = {
        'XXS': '2XS',
        'XS': 'XS',
        'S': 'S',
        'M': 'M',
        'L': 'L',
        'XL': 'XL',
        'XXL': '2XL',
        'XXXL': '3XL',
        'XXXXL': '4XL',
        'XXXXXL': '5XL',
        'XXXXXXL': '6XL',
    }
    
    # Loop through each variant
    for variant in variants:
        try:
            # Extract the first item (color-size info)
            color_size = variant[0]
            
            # Split the color and size
            color, size = color_size.split('-')
            
            # If size is a known abbreviation, map it to full name
            if size in size_mapping:
                size = size_mapping[size]
            else:
                # For sizes not there etc., leave as it is
                size = size
            
            # Initialize color in dictionary if not already present
            if color not in colors:
                colors[color] = []
            
            # Append the size to the corresponding color key
            colors[color].append(size)
        
        except Exception as e:
            # Print the error message and variant causing the issue
            print(f"Error processing variant '{variant}': {e}")
    
    # Add a 'total' key with the count of color keys
    colors_total = len(colors)
    
    return [colors, colors_total]
