data "external" "example" {
  program = ["python", "./example.py"]

  query = {
    # arbitrary map from strings to strings, passed
    # to the external program as the data query.
    id = "abc123"
  }
}

# print out to take a look
output "result" {
  value = "${data.external.example.result}"
}
