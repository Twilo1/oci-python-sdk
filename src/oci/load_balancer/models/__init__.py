# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .add_http_request_header_rule import AddHttpRequestHeaderRule
from .add_http_response_header_rule import AddHttpResponseHeaderRule
from .backend import Backend
from .backend_details import BackendDetails
from .backend_health import BackendHealth
from .backend_set import BackendSet
from .backend_set_details import BackendSetDetails
from .backend_set_health import BackendSetHealth
from .certificate import Certificate
from .certificate_details import CertificateDetails
from .connection_configuration import ConnectionConfiguration
from .create_backend_details import CreateBackendDetails
from .create_backend_set_details import CreateBackendSetDetails
from .create_certificate_details import CreateCertificateDetails
from .create_hostname_details import CreateHostnameDetails
from .create_listener_details import CreateListenerDetails
from .create_load_balancer_details import CreateLoadBalancerDetails
from .create_path_route_set_details import CreatePathRouteSetDetails
from .create_rule_set_details import CreateRuleSetDetails
from .extend_http_request_header_value_rule import ExtendHttpRequestHeaderValueRule
from .extend_http_response_header_value_rule import ExtendHttpResponseHeaderValueRule
from .health_check_result import HealthCheckResult
from .health_checker import HealthChecker
from .health_checker_details import HealthCheckerDetails
from .hostname import Hostname
from .hostname_details import HostnameDetails
from .ip_address import IpAddress
from .listener import Listener
from .listener_details import ListenerDetails
from .load_balancer import LoadBalancer
from .load_balancer_health import LoadBalancerHealth
from .load_balancer_health_summary import LoadBalancerHealthSummary
from .load_balancer_policy import LoadBalancerPolicy
from .load_balancer_protocol import LoadBalancerProtocol
from .load_balancer_shape import LoadBalancerShape
from .path_match_type import PathMatchType
from .path_route import PathRoute
from .path_route_set import PathRouteSet
from .path_route_set_details import PathRouteSetDetails
from .remove_http_request_header_rule import RemoveHttpRequestHeaderRule
from .remove_http_response_header_rule import RemoveHttpResponseHeaderRule
from .rule import Rule
from .rule_set import RuleSet
from .rule_set_details import RuleSetDetails
from .ssl_configuration import SSLConfiguration
from .ssl_configuration_details import SSLConfigurationDetails
from .session_persistence_configuration_details import SessionPersistenceConfigurationDetails
from .update_backend_details import UpdateBackendDetails
from .update_backend_set_details import UpdateBackendSetDetails
from .update_health_checker_details import UpdateHealthCheckerDetails
from .update_hostname_details import UpdateHostnameDetails
from .update_listener_details import UpdateListenerDetails
from .update_load_balancer_details import UpdateLoadBalancerDetails
from .update_network_security_groups_details import UpdateNetworkSecurityGroupsDetails
from .update_path_route_set_details import UpdatePathRouteSetDetails
from .update_rule_set_details import UpdateRuleSetDetails
from .work_request import WorkRequest
from .work_request_error import WorkRequestError

# Maps type names to classes for load_balancer services.
load_balancer_type_mapping = {
    "AddHttpRequestHeaderRule": AddHttpRequestHeaderRule,
    "AddHttpResponseHeaderRule": AddHttpResponseHeaderRule,
    "Backend": Backend,
    "BackendDetails": BackendDetails,
    "BackendHealth": BackendHealth,
    "BackendSet": BackendSet,
    "BackendSetDetails": BackendSetDetails,
    "BackendSetHealth": BackendSetHealth,
    "Certificate": Certificate,
    "CertificateDetails": CertificateDetails,
    "ConnectionConfiguration": ConnectionConfiguration,
    "CreateBackendDetails": CreateBackendDetails,
    "CreateBackendSetDetails": CreateBackendSetDetails,
    "CreateCertificateDetails": CreateCertificateDetails,
    "CreateHostnameDetails": CreateHostnameDetails,
    "CreateListenerDetails": CreateListenerDetails,
    "CreateLoadBalancerDetails": CreateLoadBalancerDetails,
    "CreatePathRouteSetDetails": CreatePathRouteSetDetails,
    "CreateRuleSetDetails": CreateRuleSetDetails,
    "ExtendHttpRequestHeaderValueRule": ExtendHttpRequestHeaderValueRule,
    "ExtendHttpResponseHeaderValueRule": ExtendHttpResponseHeaderValueRule,
    "HealthCheckResult": HealthCheckResult,
    "HealthChecker": HealthChecker,
    "HealthCheckerDetails": HealthCheckerDetails,
    "Hostname": Hostname,
    "HostnameDetails": HostnameDetails,
    "IpAddress": IpAddress,
    "Listener": Listener,
    "ListenerDetails": ListenerDetails,
    "LoadBalancer": LoadBalancer,
    "LoadBalancerHealth": LoadBalancerHealth,
    "LoadBalancerHealthSummary": LoadBalancerHealthSummary,
    "LoadBalancerPolicy": LoadBalancerPolicy,
    "LoadBalancerProtocol": LoadBalancerProtocol,
    "LoadBalancerShape": LoadBalancerShape,
    "PathMatchType": PathMatchType,
    "PathRoute": PathRoute,
    "PathRouteSet": PathRouteSet,
    "PathRouteSetDetails": PathRouteSetDetails,
    "RemoveHttpRequestHeaderRule": RemoveHttpRequestHeaderRule,
    "RemoveHttpResponseHeaderRule": RemoveHttpResponseHeaderRule,
    "Rule": Rule,
    "RuleSet": RuleSet,
    "RuleSetDetails": RuleSetDetails,
    "SSLConfiguration": SSLConfiguration,
    "SSLConfigurationDetails": SSLConfigurationDetails,
    "SessionPersistenceConfigurationDetails": SessionPersistenceConfigurationDetails,
    "UpdateBackendDetails": UpdateBackendDetails,
    "UpdateBackendSetDetails": UpdateBackendSetDetails,
    "UpdateHealthCheckerDetails": UpdateHealthCheckerDetails,
    "UpdateHostnameDetails": UpdateHostnameDetails,
    "UpdateListenerDetails": UpdateListenerDetails,
    "UpdateLoadBalancerDetails": UpdateLoadBalancerDetails,
    "UpdateNetworkSecurityGroupsDetails": UpdateNetworkSecurityGroupsDetails,
    "UpdatePathRouteSetDetails": UpdatePathRouteSetDetails,
    "UpdateRuleSetDetails": UpdateRuleSetDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError
}
