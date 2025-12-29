#!/bin/bash
# Build script for Vercel deployment
# This script builds the Hugo site and ensures the API directory is included

echo "Building Hugo site..."
echo "PEXELS_API_KEY is set: ${PEXELS_API_KEY:+YES}"

# Run Hugo build
hugo --minify

echo "Build completed!"