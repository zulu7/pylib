test_crypto:
	@./test_stream_crypto.py -e < Makefile > test.enc
	@./test_stream_crypto.py -d < test.enc > test.dec
	@md5sum Makefile | tr -s ' ' | cut -d ' ' -f 1
	@md5sum test.dec | tr -s ' ' | cut -d ' ' -f 1
	@rm -f test.enc test.dec

clean:
	find . -name '*~' -exec rm -f {} +
	find . -name '*.swp' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
