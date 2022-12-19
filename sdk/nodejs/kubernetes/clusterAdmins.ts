// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import * as pulumiKubernetes from "@pulumi/kubernetes";

/**
 * ClusterAdmins is a component that create the resources in the Cluster for a set of AWS IAM Users and Roles, managing the access with the integration with AWS IAM.
 */
export class ClusterAdmins extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'cloud-toolkit-aws:kubernetes:ClusterAdmins';

    /**
     * Returns true if the given object is an instance of ClusterAdmins.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterAdmins {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterAdmins.__pulumiType;
    }

    /**
     * The Kubernetes ClusterRoleBinding to associate the ClusterRole to the project.
     */
    public /*out*/ readonly clusterRoleBinding!: pulumi.Output<pulumiKubernetes.rbac.v1.ClusterRoleBinding>;
    /**
     * The Kubernetes provider used to provision Kubernetes resources.
     */
    public /*out*/ readonly provider!: pulumi.Output<pulumiKubernetes.Provider>;

    /**
     * Create a ClusterAdmins resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ClusterAdminsArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.kubeconfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'kubeconfig'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.userArns === undefined) && !opts.urn) {
                throw new Error("Missing required property 'userArns'");
            }
            resourceInputs["kubeconfig"] = args ? args.kubeconfig : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["userArns"] = args ? args.userArns : undefined;
            resourceInputs["clusterRoleBinding"] = undefined /*out*/;
            resourceInputs["provider"] = undefined /*out*/;
        } else {
            resourceInputs["clusterRoleBinding"] = undefined /*out*/;
            resourceInputs["provider"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ClusterAdmins.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a ClusterAdmins resource.
 */
export interface ClusterAdminsArgs {
    /**
     * Kubernetes provider used by Pulumi.
     */
    kubeconfig: pulumi.Input<string>;
    /**
     * The name for the group of Cluster Admins.
     */
    name: pulumi.Input<string>;
    /**
     * The list of AWS IAM User arns.
     */
    userArns: pulumi.Input<pulumi.Input<string>[]>;
}
