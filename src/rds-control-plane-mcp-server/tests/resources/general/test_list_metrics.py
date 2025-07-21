# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for list_metrics resource."""

import pytest
from awslabs.rds_control_plane_mcp_server.resources.general.list_metrics import (
    ListMetricItem,
    list_metrics,
    list_rds_metrics,
)


class TestListMetricItem:
    """Tests for the ListMetricItem model."""

    def test_format_metric(self):
        """Test the format_metric classmethod correctly creates a ListMetricItem."""
        metric_dict = {'MetricName': 'CPUUtilization'}
        result = ListMetricItem.format_metric(metric_dict)

        assert isinstance(result, ListMetricItem)
        assert result.namespace == 'AWS/RDS'
        assert result.metric_name == 'CPUUtilization'


class TestListMetrics:
    """Tests for the list_metrics utility function."""

    @pytest.mark.asyncio
    async def test_list_metrics(self, mock_cloudwatch_client):
        """Test list_metrics correctly calls CloudWatch API and processes results."""
        mock_cloudwatch_client.get_paginator.return_value.paginate.return_value = [
            {
                'Metrics': [
                    {'MetricName': 'CPUUtilization'},
                    {'MetricName': 'DatabaseConnections'},
                ]
            }
        ]

        result = await list_metrics('DBInstanceIdentifier', 'test-instance')

        assert len(result) == 2
        assert result[0].metric_name == 'CPUUtilization'
        assert result[1].metric_name == 'DatabaseConnections'

        mock_cloudwatch_client.get_paginator.assert_called_once_with('list_metrics')
        mock_cloudwatch_client.get_paginator.return_value.paginate.assert_called_once()
        call_args = mock_cloudwatch_client.get_paginator.return_value.paginate.call_args[1]
        assert call_args['Namespace'] == 'AWS/RDS'
        assert call_args['Dimensions'] == [
            {'Name': 'DBInstanceIdentifier', 'Value': 'test-instance'}
        ]


class TestListRDSMetrics:
    """Tests for the list_rds_metrics resource function."""

    @pytest.mark.asyncio
    async def test_list_instance_metrics(self, mock_cloudwatch_client):
        """Test list_rds_metrics correctly handles db-instance resource type."""
        mock_cloudwatch_client.get_paginator.return_value.paginate.return_value = [
            {
                'Metrics': [
                    {'MetricName': 'CPUUtilization'},
                ]
            }
        ]

        result = await list_rds_metrics('db-instance', 'test-instance')

        assert len(result) == 1
        assert result[0].metric_name == 'CPUUtilization'

        call_args = mock_cloudwatch_client.get_paginator.return_value.paginate.call_args[1]
        assert call_args['Dimensions'] == [
            {'Name': 'DBInstanceIdentifier', 'Value': 'test-instance'}
        ]

    @pytest.mark.asyncio
    async def test_list_cluster_metrics(self, mock_cloudwatch_client):
        """Test list_rds_metrics correctly handles db-cluster resource type."""
        mock_cloudwatch_client.get_paginator.return_value.paginate.return_value = [
            {
                'Metrics': [
                    {'MetricName': 'CPUUtilization'},
                ]
            }
        ]

        result = await list_rds_metrics('db-cluster', 'test-cluster')

        assert len(result) == 1
        assert result[0].metric_name == 'CPUUtilization'

        call_args = mock_cloudwatch_client.get_paginator.return_value.paginate.call_args[1]
        assert call_args['Dimensions'] == [
            {'Name': 'DBClusterIdentifier', 'Value': 'test-cluster'}
        ]
