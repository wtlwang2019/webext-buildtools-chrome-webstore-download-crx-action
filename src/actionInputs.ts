import { actionInputs as inputs, transformIfSet } from 'github-actions-utils';

export const actionInputs = {
    extensionId: inputs.getString('extensionId', true),

    crxFilePath: inputs.getWsPath('crxFilePath', true),
    prodVersion: inputs.getString('prodVersion', true),
    acceptFormat: transformIfSet(inputs.getString('acceptFormat', true), s => s.split('|')),
    platformOs: inputs.getString('platformOs', false),
    platformArch: inputs.getString('platformArch', false),
    platformNaclArch: inputs.getString('platformNaclArch', false),
}