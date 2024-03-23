#!/bin/bash

cd experiments

> ../results.txt


for file in simSwapWithTrustedOperator.spthy simSwapWithUntrustedOperator.spthy simSwapWithSocialAuthentication.spthy; do
    echo "Running Tamarin Prover for $file..."
    tamarin-prover --prove "$file" >> ../results.txt
done

echo "Tamarin Prover analysis completed. Results saved to results.txt."
