# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network vpn-gateway nat-rule create",
)
class Create(AAZCommand):
    """Create a nat rule to a scalable vpn gateway if it doesn't exist else updates the existing nat rules.

    :example: Create a nat rule.
        az network vpn-gateway nat-rule create -g MyResourceGroup --gateway-name MyVpnGateway --name MyNatRule --internal-mappings [{"address-space":10.4.0.0/24}] --external-mappings [{"address-space":192.168.21.0/24}] --type Static --mode EgressSnat
    """

    _aaz_info = {
        "version": "2023-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/vpngateways/{}/natrules/{}", "2023-09-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.gateway_name = AAZStrArg(
            options=["--gateway-name"],
            help="The name of the gateway.",
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the nat rule.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "NatRuleParameters"

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.external_mappings = AAZListArg(
            options=["--external-mappings"],
            arg_group="Properties",
            help="The private IP address external mapping for NAT.",
        )
        _args_schema.internal_mappings = AAZListArg(
            options=["--internal-mappings"],
            arg_group="Properties",
            help="The private IP address internal mapping for NAT.",
        )
        _args_schema.ip_config_id = AAZStrArg(
            options=["--ip-config-id"],
            arg_group="Properties",
            help="The IP Configuration ID this NAT rule applies to.",
        )
        _args_schema.mode = AAZStrArg(
            options=["--mode"],
            arg_group="Properties",
            help="The Source NAT direction of a VPN NAT.",
            enum={"EgressSnat": "EgressSnat", "IngressSnat": "IngressSnat"},
        )
        _args_schema.type = AAZStrArg(
            options=["--type"],
            arg_group="Properties",
            help="The type of NAT rule for VPN NAT.",
            enum={"Dynamic": "Dynamic", "Static": "Static"},
        )

        external_mappings = cls._args_schema.external_mappings
        external_mappings.Element = AAZObjectArg()
        cls._build_args_vpn_nat_rule_mapping_create(external_mappings.Element)

        internal_mappings = cls._args_schema.internal_mappings
        internal_mappings.Element = AAZObjectArg()
        cls._build_args_vpn_nat_rule_mapping_create(internal_mappings.Element)
        return cls._args_schema

    _args_vpn_nat_rule_mapping_create = None

    @classmethod
    def _build_args_vpn_nat_rule_mapping_create(cls, _schema):
        if cls._args_vpn_nat_rule_mapping_create is not None:
            _schema.address_space = cls._args_vpn_nat_rule_mapping_create.address_space
            _schema.port_range = cls._args_vpn_nat_rule_mapping_create.port_range
            return

        cls._args_vpn_nat_rule_mapping_create = AAZObjectArg()

        vpn_nat_rule_mapping_create = cls._args_vpn_nat_rule_mapping_create
        vpn_nat_rule_mapping_create.address_space = AAZStrArg(
            options=["address-space"],
            help="Address space for Vpn NatRule mapping.",
        )
        vpn_nat_rule_mapping_create.port_range = AAZStrArg(
            options=["port-range"],
            help="Port range for Vpn NatRule mapping.",
        )

        _schema.address_space = cls._args_vpn_nat_rule_mapping_create.address_space
        _schema.port_range = cls._args_vpn_nat_rule_mapping_create.port_range

    def _execute_operations(self):
        self.pre_operations()
        yield self.NatRulesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NatRulesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/natRules/{natRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "gatewayName", self.ctx.args.gateway_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "natRuleName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("externalMappings", AAZListType, ".external_mappings")
                properties.set_prop("internalMappings", AAZListType, ".internal_mappings")
                properties.set_prop("ipConfigurationId", AAZStrType, ".ip_config_id")
                properties.set_prop("mode", AAZStrType, ".mode")
                properties.set_prop("type", AAZStrType, ".type")

            external_mappings = _builder.get(".properties.externalMappings")
            if external_mappings is not None:
                _CreateHelper._build_schema_vpn_nat_rule_mapping_create(external_mappings.set_elements(AAZObjectType, "."))

            internal_mappings = _builder.get(".properties.internalMappings")
            if internal_mappings is not None:
                _CreateHelper._build_schema_vpn_nat_rule_mapping_create(internal_mappings.set_elements(AAZObjectType, "."))

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.id = AAZStrType()
            _schema_on_200_201.name = AAZStrType()
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.egress_vpn_site_link_connections = AAZListType(
                serialized_name="egressVpnSiteLinkConnections",
                flags={"read_only": True},
            )
            properties.external_mappings = AAZListType(
                serialized_name="externalMappings",
            )
            properties.ingress_vpn_site_link_connections = AAZListType(
                serialized_name="ingressVpnSiteLinkConnections",
                flags={"read_only": True},
            )
            properties.internal_mappings = AAZListType(
                serialized_name="internalMappings",
            )
            properties.ip_configuration_id = AAZStrType(
                serialized_name="ipConfigurationId",
            )
            properties.mode = AAZStrType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.type = AAZStrType()

            egress_vpn_site_link_connections = cls._schema_on_200_201.properties.egress_vpn_site_link_connections
            egress_vpn_site_link_connections.Element = AAZObjectType()
            _CreateHelper._build_schema_sub_resource_read(egress_vpn_site_link_connections.Element)

            external_mappings = cls._schema_on_200_201.properties.external_mappings
            external_mappings.Element = AAZObjectType()
            _CreateHelper._build_schema_vpn_nat_rule_mapping_read(external_mappings.Element)

            ingress_vpn_site_link_connections = cls._schema_on_200_201.properties.ingress_vpn_site_link_connections
            ingress_vpn_site_link_connections.Element = AAZObjectType()
            _CreateHelper._build_schema_sub_resource_read(ingress_vpn_site_link_connections.Element)

            internal_mappings = cls._schema_on_200_201.properties.internal_mappings
            internal_mappings.Element = AAZObjectType()
            _CreateHelper._build_schema_vpn_nat_rule_mapping_read(internal_mappings.Element)

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_vpn_nat_rule_mapping_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("addressSpace", AAZStrType, ".address_space")
        _builder.set_prop("portRange", AAZStrType, ".port_range")

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id

    _schema_vpn_nat_rule_mapping_read = None

    @classmethod
    def _build_schema_vpn_nat_rule_mapping_read(cls, _schema):
        if cls._schema_vpn_nat_rule_mapping_read is not None:
            _schema.address_space = cls._schema_vpn_nat_rule_mapping_read.address_space
            _schema.port_range = cls._schema_vpn_nat_rule_mapping_read.port_range
            return

        cls._schema_vpn_nat_rule_mapping_read = _schema_vpn_nat_rule_mapping_read = AAZObjectType()

        vpn_nat_rule_mapping_read = _schema_vpn_nat_rule_mapping_read
        vpn_nat_rule_mapping_read.address_space = AAZStrType(
            serialized_name="addressSpace",
        )
        vpn_nat_rule_mapping_read.port_range = AAZStrType(
            serialized_name="portRange",
        )

        _schema.address_space = cls._schema_vpn_nat_rule_mapping_read.address_space
        _schema.port_range = cls._schema_vpn_nat_rule_mapping_read.port_range


__all__ = ["Create"]
