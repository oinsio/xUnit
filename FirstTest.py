from xUnit import WasRun

test = WasRun("test_method")
print(test.wasRun)
test.run()
print(test.wasRun)