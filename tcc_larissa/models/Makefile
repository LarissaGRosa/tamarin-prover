TARGETS = $(wildcard experiments/*.spthy)
EXT := .proof
PROOFS = $(addsuffix $(EXT), $(TARGETS))

prove: $(PROOFS)

%.spthy$(EXT): %.spthy
	tamarin-prover --prove "$<" --output="$@"

clean:
	$(RM) $(PROOFS)
