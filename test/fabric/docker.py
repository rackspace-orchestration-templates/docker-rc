from fabric.api import env, task
from envassert import detect, file, package, process, service
from hot.utils.test import get_artifacts


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("lxc-docker")
    assert file.exists("/etc/default/docker")
    assert file.exists("/var/run/docker.sock")
    assert process.is_up("docker")
    assert service.is_enabled("docker")


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
