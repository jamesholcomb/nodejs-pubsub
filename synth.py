import synthtool as s
import synthtool.gcp as gcp
import logging
import subprocess

logging.basicConfig(level=logging.DEBUG)

gapic = gcp.GAPICGeneratorgcp.CommonTemplates()
()

# tasks has two product names, and a poorly named artman yaml
version = 'v1'
library = gapic.node_library(
    'pubsub', version, config_path="/google/pubsub/artman_pubsub.yaml")

# skip index, protos, package.json, and README.md
s.copy(
    library,
    excludes=['package.json', 'README.md', 'src/index.js'])

templates = common_templates.node_library(package_name="@google-cloud/pubsub")
s.copy(templates)


# https://github.com/googleapis/gapic-generator/issues/2127
s.replace("src/v1/subscriber_client.js",
          "  }\n\s*/\*\*\n\s+\* The DNS address for this API service.",
          "\n    // note: editing generated code\n"
          "    this.waitForReady = function(deadline, callback) {\n"
          "      return subscriberStub.then(\n"
          "        stub => stub.waitForReady(deadline, callback),\n"
          "        callback\n"
          "      );\n"
          "    };\n"
          "\g<0>")

# Node.js specific cleanup
subprocess.run(['npm', 'ci'])
subprocess.run(['npm', 'run', 'prettier'])
subprocess.run(['npm', 'run', 'lint'])
