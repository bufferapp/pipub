import click
from google.cloud import pubsub_v1 as pubsub
from google.cloud.pubsub_v1.types import BatchSettings


def standard_input():
    """Generator that yields lines from standard input."""
    with click.get_text_stream("stdin") as stdin:
        while stdin.readable():
            line = stdin.readline()
            if line:
                yield line.strip().encode("utf-8")


@click.command()
@click.argument("topic", type=str)
@click.option("--google-cloud-project", "-p", envvar="GOOGLE_CLOUD_PROJECT")
@click.option("--batch-size", "-b", default=500)
def run(topic, google_cloud_project, batch_size):
    publisher = pubsub.PublisherClient(
        batch_settings=BatchSettings(max_messages=batch_size)
    )

    topic_path = publisher.topic_path(google_cloud_project, topic)

    for line in standard_input():
        publisher.publish(topic_path, data=line)


if __name__ == "__main__":
    run()
