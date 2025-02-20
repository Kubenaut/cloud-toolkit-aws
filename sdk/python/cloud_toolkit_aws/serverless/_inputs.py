# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'CdnCacheArgs',
    'CdnDnsArgs',
    'DeadLetterQueueTypeArgs',
    'QueueArgs',
]

@pulumi.input_type
class CdnCacheArgs:
    def __init__(__self__, *,
                 ttl: pulumi.Input[float]):
        """
        :param pulumi.Input[float] ttl: Cloud Front distribution cache time to live
        """
        pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Input[float]:
        """
        Cloud Front distribution cache time to live
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: pulumi.Input[float]):
        pulumi.set(self, "ttl", value)


@pulumi.input_type
class CdnDnsArgs:
    def __init__(__self__, *,
                 ttl: pulumi.Input[float]):
        """
        :param pulumi.Input[float] ttl: DNS time to live
        """
        pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Input[float]:
        """
        DNS time to live
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: pulumi.Input[float]):
        pulumi.set(self, "ttl", value)


@pulumi.input_type
class DeadLetterQueueTypeArgs:
    def __init__(__self__, *,
                 enable: pulumi.Input[bool],
                 type: pulumi.Input['DeadLetterQueueTypes'],
                 existing_dead_letter_queue_arn: Optional[pulumi.Input[str]] = None,
                 message_retention_seconds: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[bool] enable: Enables the feature.
        :param pulumi.Input['DeadLetterQueueTypes'] type: Dead Letter Queue type attached to the component to create.
        :param pulumi.Input[str] existing_dead_letter_queue_arn: Placing a Queue ARN will set said already existing Queue as a Dead Letter Queue for the new one.
        :param pulumi.Input[float] message_retention_seconds: The amount of time that a message will be stored in the Dead Letter Queue without being deleted. Minimum is 60 seconds (1 minutes) and Maximum 1,209,600 (14 days) seconds. By default a message is retained 4 days.
        """
        pulumi.set(__self__, "enable", enable)
        pulumi.set(__self__, "type", type)
        if existing_dead_letter_queue_arn is not None:
            pulumi.set(__self__, "existing_dead_letter_queue_arn", existing_dead_letter_queue_arn)
        if message_retention_seconds is not None:
            pulumi.set(__self__, "message_retention_seconds", message_retention_seconds)

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Input[bool]:
        """
        Enables the feature.
        """
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['DeadLetterQueueTypes']:
        """
        Dead Letter Queue type attached to the component to create.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['DeadLetterQueueTypes']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="existingDeadLetterQueueArn")
    def existing_dead_letter_queue_arn(self) -> Optional[pulumi.Input[str]]:
        """
        Placing a Queue ARN will set said already existing Queue as a Dead Letter Queue for the new one.
        """
        return pulumi.get(self, "existing_dead_letter_queue_arn")

    @existing_dead_letter_queue_arn.setter
    def existing_dead_letter_queue_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "existing_dead_letter_queue_arn", value)

    @property
    @pulumi.getter(name="messageRetentionSeconds")
    def message_retention_seconds(self) -> Optional[pulumi.Input[float]]:
        """
        The amount of time that a message will be stored in the Dead Letter Queue without being deleted. Minimum is 60 seconds (1 minutes) and Maximum 1,209,600 (14 days) seconds. By default a message is retained 4 days.
        """
        return pulumi.get(self, "message_retention_seconds")

    @message_retention_seconds.setter
    def message_retention_seconds(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "message_retention_seconds", value)


@pulumi.input_type
class QueueArgs:
    def __init__(__self__, *,
                 dead_letter_queue_type_args: Optional[pulumi.Input['DeadLetterQueueTypeArgs']] = None,
                 is_fifo: Optional[pulumi.Input[bool]] = None,
                 max_message_size: Optional[pulumi.Input[float]] = None,
                 message_retention_seconds: Optional[pulumi.Input[float]] = None,
                 policy: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['DeadLetterQueueTypeArgs'] dead_letter_queue_type_args: Dead Letter Queue attached to the component to create.
        :param pulumi.Input[bool] is_fifo: Set to true to create the Queue as FiFo. False for a Standard Queue.
        :param pulumi.Input[float] max_message_size: The limit for a Queue message size in bytes. Minimum is 1 byte (1 character) and Maximum 262,144 bytes (256 KiB). By default a message can be 256 KiB large.
        :param pulumi.Input[float] message_retention_seconds: The amount of time that a message will be stored in the Queue without being deleted. Minimum is 60 seconds (1 minutes) and Maximum 1,209,600 (14 days) seconds. By default a message is retained 4 days.
        :param pulumi.Input[str] policy: Custom policy for the Queue.
        """
        if dead_letter_queue_type_args is not None:
            pulumi.set(__self__, "dead_letter_queue_type_args", dead_letter_queue_type_args)
        if is_fifo is not None:
            pulumi.set(__self__, "is_fifo", is_fifo)
        if max_message_size is not None:
            pulumi.set(__self__, "max_message_size", max_message_size)
        if message_retention_seconds is not None:
            pulumi.set(__self__, "message_retention_seconds", message_retention_seconds)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)

    @property
    @pulumi.getter(name="DeadLetterQueueTypeArgs")
    def dead_letter_queue_type_args(self) -> Optional[pulumi.Input['DeadLetterQueueTypeArgs']]:
        """
        Dead Letter Queue attached to the component to create.
        """
        return pulumi.get(self, "dead_letter_queue_type_args")

    @dead_letter_queue_type_args.setter
    def dead_letter_queue_type_args(self, value: Optional[pulumi.Input['DeadLetterQueueTypeArgs']]):
        pulumi.set(self, "dead_letter_queue_type_args", value)

    @property
    @pulumi.getter(name="isFifo")
    def is_fifo(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to true to create the Queue as FiFo. False for a Standard Queue.
        """
        return pulumi.get(self, "is_fifo")

    @is_fifo.setter
    def is_fifo(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_fifo", value)

    @property
    @pulumi.getter(name="maxMessageSize")
    def max_message_size(self) -> Optional[pulumi.Input[float]]:
        """
        The limit for a Queue message size in bytes. Minimum is 1 byte (1 character) and Maximum 262,144 bytes (256 KiB). By default a message can be 256 KiB large.
        """
        return pulumi.get(self, "max_message_size")

    @max_message_size.setter
    def max_message_size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_message_size", value)

    @property
    @pulumi.getter(name="messageRetentionSeconds")
    def message_retention_seconds(self) -> Optional[pulumi.Input[float]]:
        """
        The amount of time that a message will be stored in the Queue without being deleted. Minimum is 60 seconds (1 minutes) and Maximum 1,209,600 (14 days) seconds. By default a message is retained 4 days.
        """
        return pulumi.get(self, "message_retention_seconds")

    @message_retention_seconds.setter
    def message_retention_seconds(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "message_retention_seconds", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        Custom policy for the Queue.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)


