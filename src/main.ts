import * as ghActions from '@actions/core';
import { actionInputs } from './actionInputs';
import { actionOutputs } from './actionOutputs';
import { DownloadCrx } from 'typed-chrome-webstore-api';
import { writeStreamToFile } from "./writeStreamToFile";

async function run(): Promise<void> {
    try {
        await runImpl();
    } catch (error) {
        ghActions.setFailed(error as Error);
    }
}

async function runImpl() {
    const readStream = await DownloadCrx.downloadCrx(
        actionInputs.extensionId,
        actionInputs.prodVersion,
        actionInputs.acceptFormat,
        getPlatformOptions()
    );
    await writeStreamToFile(actionInputs.crxFilePath, readStream);
    actionOutputs.crxFilePath.setValue(actionInputs.crxFilePath);
}

function getPlatformOptions(): DownloadCrx.IPlatformRequest|undefined {
    if (actionInputs.platformArch && actionInputs.platformOs && actionInputs.platformNaclArch) {
        return {
            arch: actionInputs.platformArch,
            os: actionInputs.platformOs,
            naclArch: actionInputs.platformNaclArch
        }
    } else if (!haveTheSameStatus(actionInputs.platformArch, actionInputs.platformOs, actionInputs.platformNaclArch)) {
        ghActions.warning('platformArch, platformOs, platformNaclArch inputs should be set together. Ignoring.');
    }

    return undefined;
}

function haveTheSameStatus(...values: any): boolean {
    if (values.length === 0) {
        return true;
    }
    let status = values[0] !== undefined;
    for (let i = 1; i < values.length; ++i) {
        if ((values[i] !== undefined) !== status) {
            return false;
        }
    }
    return true;
}

// noinspection JSIgnoredPromiseFromCall
run();