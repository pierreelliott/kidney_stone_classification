import * as tf from '@tensorflow/tfjs';
import {loadGraphModel} from '@tensorflow/tfjs-converter';
import { API_BASEURL } from "./classifierAPI";

const MODEL_URL = `${API_BASEURL}/model/model.json`;

const classifier = (function() {
    var classif = undefined;
    return async function () {
        if (!classif) {
            classif = await loadGraphModel(MODEL_URL);
        }
        return classif;
    }
})();

export const useLocalClassifier = async function(image) {
    const model = await classifier();
    const result = model.execute(tf.fromPixels(image));
    // eslint-disable-next-line no-console
    console.warn(result);
    return result;
};
