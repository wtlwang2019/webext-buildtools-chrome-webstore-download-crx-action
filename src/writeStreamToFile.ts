import {Readable, Stream} from "stream";
import path from "path";
import * as fs from 'fs-extra';

function writeFinished(stream: Stream) {
    return new Promise((resolve, reject) => {
        stream.on('finish', resolve);
        stream.on('error', reject);
    });
}

async function writeToFile(filePath: string, src: Buffer | Readable) {
    try {
        if (Buffer.isBuffer(src)) {
            await fs.writeFile(filePath, src);
        } else {
            const writeStream = fs.createWriteStream(filePath);
            src.pipe(writeStream);
            src.on('error', err => {
                writeStream.emit('error', err);
            });
            await writeFinished(writeStream);
        }
    } catch (error) {
        try {
            await fs.unlink(filePath);
        } catch (error) {}
        throw error;
    }
}

export async function writeStreamToFile(
    filePath: string,
    src: Buffer | Readable,
): Promise<any> {
    await fs.ensureDir(path.dirname(filePath));
    return writeToFile(filePath, src);
}