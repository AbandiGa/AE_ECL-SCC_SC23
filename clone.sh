#!/bin/bash 


# Set the array of Git repository URLs
repos=(
    "https://github.com/iHeartGraph/iSpan.git"
    "https://github.com/chenxuhao/gpuscc_code.git"
)

# Set the array of output directories
output_dirs=(
    "~/SCC/codes/iSpan"
    "~/SCC/codes/GPU_SCC"
)

# Iterate over the repositories
for i in "${!repos[@]}"; do
    # Clone the repository into the corresponding output directory
    git clone "${repos[$i]}" "${output_dirs[$i]}"
done


exit 0 